import customtkinter as ctk
from src.presentation.styles import *

class PracticeMenu(ctk.CTkFrame):
    def __init__(self, master, on_back, on_select_level, progress_use_case):
        super().__init__(master, fg_color="transparent")
        
        ctk.CTkButton(
            self, 
            text="< Voltar", 
            command=on_back, 
            width=100,
            font=font_button()
        ).pack(anchor="nw", padx=40, pady=40)
        
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            main_frame, 
            text="Escolha o Nível", 
            font=font_title_medium()
        ).pack(pady=40)

        levels = ["facil", "medio", "dificil"]
        labels = ["Fácil", "Médio", "Difícil"]
        colors = [COLOR_SUCCESS, COLOR_ORANGE, COLOR_ERROR]

        for level, label, color in zip(levels, labels, colors):
            is_unlocked = progress_use_case.is_practice_level_unlocked(level)
            
            state = "normal" if is_unlocked else "disabled"
            display_color = color if is_unlocked else "gray"
            display_text = label if is_unlocked else f"{label} (Bloqueado)"

            ctk.CTkButton(
                main_frame,
                text=display_text,
                width=300, 
                height=80,
                font=font_button(),
                fg_color=display_color,
                state=state,
                
                command=lambda l=level: on_select_level(l)
            ).pack(pady=15)