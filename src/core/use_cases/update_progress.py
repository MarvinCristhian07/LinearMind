from src.core.entities.user_progress import UserProgress
from src.infrastructure.persistence.progress_repository import ProgressRepository
from src.infrastructure.content.lessons_data import LESSONS_ORDER
from src.infrastructure.content.exercises_data import EXERCISES_ORDER

class UpdateProgress:
    def __init__(self, repository: ProgressRepository):
        self.repositoy = repository
        self.progress = self.repositoy.load_progress()

    def get_progress(self) -> UserProgress:
        return self.progress
    
    def complete_lesson(self, lesson_id: str):
        self.progress.complete_lesson(lesson_id)
        self.repositoy.save_progress(self.progress)

    def complete_exercise(self, exercise_id: str):
        self.progress.complete_exercise(exercise_id)
        self.repositoy.save_progress(self.progress)

    def is_lesson_unlocked(self, lesson_id: str) -> bool:
        # Lição X só desbloqueia se lição X-1 foi concluída
        try:
            index = LESSONS_ORDER.index(lesson_id)
        except ValueError:
            return False
        
        if index == 0:
            return True
        
        previous_lesson_id = LESSONS_ORDER[index - 1]

        return self.progress.has_completed_lesson(previous_lesson_id)

    def is_practice_level_unlocked(self, level: str) -> bool:
        """
        facil: sempre desbloqueado
        medio: todos os facil completos
        dificil: todos os facil e medio completos
        """
        if level == "facil":
            return True
        
        if level == "medio":
            easy_exercises = EXERCISES_ORDER.get("facil", [])
            if not easy_exercises:
                return True
            
            return all(self.progress.has_completed_exercise(ex_id) for ex_id in easy_exercises)
        
        if level == "dificil":
            medium_exercises = EXERCISES_ORDER.get("medio", [])
            if not medium_exercises:
                return True
            
            return all(self.progress.has_completed_exercise(ex_id) for ex_id in medium_exercises)
        
        return False