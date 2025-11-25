import customtkinter as ctk
from PIL import Image
import os
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
        container.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(container, text=self.lesson.title, font=ctk.CTkFont(size=24, weight="bold"), text_color="gray").pack(pady=(0, 20))

        # Área de Conteúdo (Imagem ou Texto)
        content_frame = ctk.CTkFrame(container, fg_color="transparent")
        content_frame.pack(expand=True, fill="both")

        if "image_path" in slide.content:
            img_path = slide.content["image_path"]
            
            if os.path.exists(img_path):
                pil_image = Image.open(img_path)
                
                screen_height = self.winfo_screenheight()
                
                target_height = int(screen_height * 0.65)
                
                if target_height <= 0: target_height = 400

                aspect_ratio = pil_image.width / pil_image.height
                target_width = int(target_height * aspect_ratio)

                if target_width <= 0: target_width = 400

                ctk_image = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(target_width, target_height))
                
                image_label = ctk.CTkLabel(content_frame, text="", image=ctk_image)
                image_label.pack(expand=True)
            else:
                ctk.CTkLabel(content_frame, text=f"Erro: Imagem não encontrada\n{img_path}", text_color=COLOR_ERROR).pack(expand=True)

        elif "text" in slide.content:
            ctk.CTkLabel(
                content_frame, 
                text=slide.content["text"], 
                font=ctk.CTkFont(size=28), 
                wraplength=800
            ).pack(expand=True)

        # Rodapé
        self.render_footer(container)

    def render_footer(self, parent):
        footer = ctk.CTkFrame(parent, height=60, fg_color="transparent")
        footer.pack(fill="x", pady=10, padx=20)

        # Botão Esquerdo
        if self.current_slide_index > 0:
            ctk.CTkButton(footer, text="Anterior", command=self.prev_slide, font=font_button()).pack(side="left")
        else:
            ctk.CTkButton(footer, text="Sair", fg_color="transparent", border_width=1, font=font_button(), 
                          command=lambda: self.on_finish_lesson(completed=False)).pack(side="left")

        # Contador
        ctk.CTkLabel(footer, text=f"Slide {self.current_slide_index + 1}/{self.total_slides}", font=font_text()).pack(side="left", expand=True)

        # Botão Direito
        if self.current_slide_index < self.total_slides - 1:
            ctk.CTkButton(footer, text="Próximo", command=self.next_slide, font=font_button()).pack(side="right")
        else:
            ctk.CTkButton(footer, text="CONCLUIR AULA", fg_color=COLOR_SUCCESS, hover_color="#25A870", font=font_button(),
                          command=lambda: self.on_finish_lesson(completed=True)).pack(side="right")

    def next_slide(self):
        self.current_slide_index += 1
        self.render_slide()

    def prev_slide(self):
        self.current_slide_index -= 1
        self.render_slide()