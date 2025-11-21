import customtkinter as ctk
from src.presentation.styles import *

class LessonViewer(ctk.CTkFrame):
    def __init__(self, master, lesson, on_finish_lesson):
        super().__init__(master)
        self.lesson = lesson
        self.on_finish_lesson = on_finish_lesson
        
        self.current_slide_index = 0
        self.total_slides = len(lesson.slides)

        self.render_slide()

    def render_slide(self):
        for widget in self.winfo_children():
            widget.destroy()

        slide = self.lesson.slides[self.current_slide_index]

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True, padx=50, pady=50)

        ctk.CTkLabel(
            container, 
            text=self.lesson.title, 
            font=ctk.CTkFont(family="Roboto", size=24, weight="bold"), 
            text_color="gray"
        ).pack(pady=20)

        content_frame = ctk.CTkFrame(container, fg_color="transparent")
        content_frame.pack(expand=True, fill="both", padx=50)
        
        # Renderiza Texto
        if "text" in slide.content:
            ctk.CTkLabel(
                content_frame, 
                text=slide.content["text"], 
                font=ctk.CTkFont(family="Roboto", size=28), 
                wraplength=800,
                justify="left"
            ).pack(expand=True)

        self.render_footer(container)

    def render_footer(self, parent):
        footer = ctk.CTkFrame(parent, height=60, fg_color="transparent")
        footer.pack(fill="x", pady=20, padx=20)

        if self.current_slide_index > 0:
            ctk.CTkButton(
                footer, 
                text="Anterior", 
                command=self.prev_slide,
                font=font_button()
            ).pack(side="left")
        else:
            ctk.CTkButton(
                footer, 
                text="Sair", 
                fg_color="transparent", 
                border_width=1, 
                font=font_button(),
                command=lambda: self.on_finish_lesson(completed=False)
            ).pack(side="left")

        ctk.CTkLabel(
            footer, 
            text=f"Slide {self.current_slide_index + 1}/{self.total_slides}",
            font=font_text()
        ).pack(side="left", expand=True)

        if self.current_slide_index < self.total_slides - 1:
            ctk.CTkButton(
                footer, 
                text="Próximo", 
                command=self.next_slide,
                font=font_button()
            ).pack(side="right")
        else:
            ctk.CTkButton(
                footer, 
                text="Concluir aula", 
                fg_color=COLOR_SUCCESS, 
                hover_color="#25A870",
                font=font_button(),
                command=lambda: self.on_finish_lesson(completed=True)
            ).pack(side="right")

    def next_slide(self):
        self.current_slide_index += 1
        self.render_slide()

    def prev_slide(self):
        self.current_slide_index -= 1
        self.render_slide()