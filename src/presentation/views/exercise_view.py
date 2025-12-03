import customtkinter as ctk
import threading
from src.presentation.styles import *

class ExerciseView(ctk.CTkFrame):
    def __init__(self, master, exercises_list, on_exit, check_use_case, progress_use_case, ai_use_case):
        super().__init__(master)
        self.exercises_list = exercises_list
        self.on_exit = on_exit
        
        self.check_use_case = check_use_case
        self.progress_use_case = progress_use_case
        self.ai_use_case = ai_use_case

        self.current_idx = 0
        self.entry_widgets = {} 

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self.setup_ui_structure()
        self.load_exercise()

    def setup_ui_structure(self):
        # Coluna da Esquerda (Problema)
        self.problem_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.problem_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # Coluna da Direita (Chatbot)
        self.chat_frame = ctk.CTkFrame(self, fg_color=COLOR_BG_DARK)
        self.chat_frame.grid(row=0, column=1, sticky="nsew", padx=(0, 20), pady=20)

        ctk.CTkLabel(self.chat_frame, text="LinearMind AI 🤖", font=font_button()).pack(pady=20)

        self.chat_scroll = ctk.CTkScrollableFrame(self.chat_frame, fg_color="transparent")
        self.chat_scroll.pack(fill="both", expand=True, padx=10, pady=10)

    def reset_chat(self):
        # Limpa o histórico do chat e adiciona mensagem inicial
        for widget in self.chat_scroll.winfo_children():
            widget.destroy()
        
        self.add_chat_message("Olá! Sou seu tutor virtual. Se errar, te darei dicas aqui!", is_user=False)

    def load_exercise(self):
        # 1. Limpa a área do problema
        for widget in self.problem_frame.winfo_children():
            widget.destroy()

        # 2. Reseta o chat para o novo exercício
        self.reset_chat()

        exercise = self.exercises_list[self.current_idx]

        # Botão Sair
        ctk.CTkButton(self.problem_frame, text="< Sair", command=self.on_exit, width=80,
                      fg_color="transparent", border_width=1, text_color="gray").pack(anchor="nw")

        ctk.CTkLabel(self.problem_frame, text=f"Exercício {self.current_idx + 1}", 
                     font=font_title_medium(), text_color="gray").pack(pady=(20, 10))
        
        ctk.CTkLabel(self.problem_frame, text=exercise.prompt, 
                     font=ctk.CTkFont(family="Roboto", size=24), 
                     wraplength=700, justify="left").pack(pady=20, padx=20)

        # Inputs
        inputs_container = ctk.CTkFrame(self.problem_frame, fg_color="transparent")
        inputs_container.pack(pady=20)
        
        self.entry_widgets = {} 
        for var_name, var_type in exercise.inputs.items():
            row = ctk.CTkFrame(inputs_container, fg_color="transparent")
            row.pack(pady=10)
            ctk.CTkLabel(row, text=f"{var_name} =", font=font_text()).pack(side="left", padx=10)
            entry = ctk.CTkEntry(row, width=150, font=font_text(), justify="center")
            entry.pack(side="left")
            self.entry_widgets[var_name] = entry

        # Botão Verificar
        self.btn_verify = ctk.CTkButton(self.problem_frame, text="VERIFICAR RESPOSTA", height=50,
                                        font=font_button(), command=self.verify_answer, fg_color=COLOR_PRIMARY)
        self.btn_verify.pack(pady=30)

        self.lbl_feedback = ctk.CTkLabel(self.problem_frame, text="", font=font_button())
        self.lbl_feedback.pack(pady=10)

    def verify_answer(self):
        exercise = self.exercises_list[self.current_idx]
        user_answers = {k: v.get() for k, v in self.entry_widgets.items()}

        is_correct, field_errors = self.check_use_case.execute(user_answers, exercise.answers)

        if is_correct:
            self.lbl_feedback.configure(text="PARABÉNS! VOCÊ ACERTOU! 👏", text_color=COLOR_SUCCESS)
            self.btn_verify.configure(text="PRÓXIMO EXERCÍCIO >", fg_color=COLOR_SUCCESS, command=self.next_exercise)
            self.progress_use_case.complete_exercise(exercise.id)
            for entry in self.entry_widgets.values():
                entry.configure(border_color=COLOR_SUCCESS)
        else:
            self.lbl_feedback.configure(text="Ops! Algo errado. Olhe a dica da IA ->", text_color=COLOR_ERROR)
            for var_name, is_ok in field_errors.items():
                if not is_ok and var_name in self.entry_widgets:
                    self.entry_widgets[var_name].configure(border_color=COLOR_ERROR)
            
            self.add_chat_message("Analisando seu erro...", is_user=False)
            threading.Thread(target=self.call_ai_thread, args=(exercise, user_answers)).start()

    def next_exercise(self):
        if self.current_idx < len(self.exercises_list) - 1:
            self.current_idx += 1
            self.load_exercise()
        else:
            self.show_level_complete()

    def show_level_complete(self):
        for widget in self.problem_frame.winfo_children():
            widget.destroy()
        
        self.reset_chat()
        
        ctk.CTkLabel(self.problem_frame, text="NÍVEL CONCLUÍDO! 🏆", font=font_title_large(), text_color=COLOR_SUCCESS).pack(expand=True)
        ctk.CTkButton(self.problem_frame, text="Voltar ao Menu", command=self.on_exit, height=50, font=font_button()).pack(pady=50)

    def call_ai_thread(self, exercise, user_answers):
        try:
            hint = self.ai_use_case.execute(exercise, user_answers)
            self.after(0, lambda: self.add_chat_message(hint, is_user=False))
        except Exception:
             self.after(0, lambda: self.add_chat_message("Erro ao conectar com a IA.", is_user=False))

    def add_chat_message(self, text, is_user=False):
        align = "e" if is_user else "w"
        color = COLOR_PRIMARY if is_user else "#404040"
        
        bubble = ctk.CTkLabel(
            self.chat_scroll, 
            text=text, 
            font=ctk.CTkFont(family="Roboto", size=16),
            fg_color=color,
            text_color="white",
            corner_radius=15,
            wraplength=300,
            justify="left",
            padx=15, pady=10
        )
        bubble.pack(anchor=align, pady=5, padx=10)
        
        self.chat_scroll.update_idletasks()
        self.chat_scroll._parent_canvas.yview_moveto(1.0)