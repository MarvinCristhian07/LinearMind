import customtkinter as ctk

COLOR_SUCCESS = "#2CC985"
COLOR_ERROR = "#FF4D4D" 
COLOR_PRIMARY = "#1f6aa5"
COLOR_BG_DARK = "#2b2b2b"
COLOR_ORANGE = "#D97834"  
COLOR_ORANGE_HOVER = "#B55F21"

def font_title_large():
    return ctk.CTkFont(family="Roboto", size=64, weight="bold")

def font_title_medium():
    return ctk.CTkFont(family="Roboto", size=32, weight="bold")

def font_button():
    return ctk.CTkFont(family="Roboto", size=20, weight="bold")

def font_text():
    return ctk.CTkFont(family="Roboto", size=20)

def font_chat_bubble():
    return ctk.CTkFont(family="Roboto", size=16)