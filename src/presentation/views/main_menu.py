import customtkinter as ctk
from src.presentation.styles import *

class MainMenu(ctk.CTkFrame):
    def __init__(self, master, on_navigate_lessons, on_navigate_practice, on_exit):
        super().__init__(master, fg_color="transparent")

        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(
            main_frame,
            text="LinearMind",
            font=font_title_large()
        ).pack(pady=(0, 10))

        ctk.CTkLabel(
            main_frame,
            text="Domine a Função Afim sem dificuldades!",
            font=ctk.CTkFont(family="Roboto", size=24)
        ).pack(pady=(0, 50))

        ctk.CTkButton(
            main_frame, 
            text="Aulas", 
            command=on_navigate_lessons,
            width=300, 
            height=60, 
            font=font_button(), 
            corner_radius=15,
            fg_color=COLOR_PRIMARY
        ).pack(pady=15)

        ctk.CTkButton(
            main_frame, 
            text="Práticas", 
            command=on_navigate_practice,
            width=300, 
            height=60, 
            font=font_button(), 
            corner_radius=15, 
            fg_color=COLOR_ORANGE, 
            hover_color=COLOR_ORANGE_HOVER
        ).pack(pady=15)

        ctk.CTkButton(
            main_frame, 
            text="Sair", 
            command=on_exit,
            width=300, 
            height=40, 
            fg_color="transparent", 
            border_width=2, 
            text_color="gray"
        ).pack(pady=30)