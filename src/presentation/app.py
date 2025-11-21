import customtkinter as ctk

# Camada de Infraestrutura (Externo)
from src.infrastructure.persistence.progress_repository import ProgressRepository
from src.infrastructure.services.gemini_service import GeminiService

# Camada de Aplicação (Regras)
from src.core.use_cases.get_content import GetContent
from src.core.use_cases.check_answer import CheckAnswer
from src.core.use_cases.update_progress import UpdateProgress
from src.core.use_cases.get_ai_hint import GetAIHint

# Camada de Apresentação (Telas)
from src.presentation.views.main_menu import MainMenu
from src.presentation.views.lessons_menu import LessonsMenu
from src.presentation.views.lesson_viewer import LessonViewer
from src.presentation.views.practice_menu import PracticeMenu
from src.presentation.views.exercise_view import ExerciseView

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LinearMind")
        self.attributes("-fullscreen", True)
        
        self.bind("<Escape>", lambda event: self.destroy())

        print("Inicializando dependências...")
        self.repo = ProgressRepository()
        
        try:
            self.gemini = GeminiService()
        except Exception as e:
            print(f"Aviso: Serviço de IA não pôde ser iniciado: {e}")
            self.gemini = None 
        
        self.uc_content = GetContent()
        self.uc_progress = UpdateProgress(self.repo)
        self.uc_check = CheckAnswer()
        self.uc_ai = GetAIHint(self.gemini) if self.gemini else None

        self.show_main_menu()

    def switch_view(self, view_class, **kwargs):
        for widget in self.winfo_children():
            widget.destroy()
        
        view = view_class(master=self, **kwargs)
        view.pack(fill="both", expand=True)

    def show_main_menu(self):
        self.switch_view(
            MainMenu, 
            on_navigate_lessons=self.show_lessons_menu,
            on_navigate_practice=self.show_practice_menu,
            on_exit=self.destroy
        )

    def show_lessons_menu(self):
        self.switch_view(
            LessonsMenu,
            on_back=self.show_main_menu,
            on_select_lesson=self.start_lesson,
            content_use_case=self.uc_content,
            progress_use_case=self.uc_progress
        )

    def start_lesson(self, lesson):
        
        def on_finish(completed):
            if completed:
                print(f"Aula concluída: {lesson.title}")
                self.uc_progress.complete_lesson(lesson.id)
            
            self.show_lessons_menu()

        self.switch_view(
            LessonViewer,
            lesson=lesson,
            on_finish_lesson=on_finish
        )

    def show_practice_menu(self):
        self.switch_view(
            PracticeMenu,
            on_back=self.show_main_menu,
            on_select_level=self.start_practice_level,
            progress_use_case=self.uc_progress
        )

    def start_practice_level(self, level):
        exercises = self.uc_content.get_exercises_by_level(level)
        
        if not exercises:
            print(f"Nenhum exercício encontrado para o nível: {level}")
            return

        self.switch_view(
            ExerciseView,
            exercises_list=exercises,
            on_exit=self.show_practice_menu,
            check_use_case=self.uc_check,
            progress_use_case=self.uc_progress,
            ai_use_case=self.uc_ai
        )

if __name__ == "__main__":
    app = App()
    app.mainloop()