import customtkinter as ctk
from src.presentation.styles import *

class LessonsMenu(ctk.CTkFrame):
    def __init__(self, master, on_back, on_select_lesson, content_use_case, progress_use_case):
        super().__init__(master, fg_color="transparent")

        header = ctk.CTkFrame(self, height=80, fg_color="transparent")
        header.pack(fill="x", padx=40, pady=20)

        ctk.CTkButton(
            header, 
            text="< Voltar", 
            command=on_back, 
            width=100,
            font=font_button()
        ).pack(side="left")

        ctk.CTkLabel(
            header, 
            text="Trilha de Aprendizado", 
            font=font_title_medium()
        ).pack(side="left", padx=20)

        grid_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True, padx=40, pady=20)

        lessons = content_use_case.get_all_lessons_in_order()
        progress = progress_use_case.get_progress()

        for i, lesson in enumerate(lessons):
            is_unlocked = progress_use_case.is_lesson_unlocked(lesson.id)
            is_completed = progress.has_completed_lesson(lesson.id)
            
            color = COLOR_PRIMARY
            state = "normal"
            text_prefix = f"{i+1}. "

            if not is_unlocked:
                color = "gray"
                state = "disabled"
                text_prefix = "🔒 "
            elif is_completed:
                color = COLOR_SUCCESS
                text_prefix = "✓ "

            ctk.CTkButton(
                grid_frame,
                text=f"{text_prefix}{lesson.title}",
                height=80,
                font=font_button(),
                fg_color=color,
                state=state,
                
                command=lambda l=lesson: on_select_lesson(l)
            ).pack(fill="x", pady=10)