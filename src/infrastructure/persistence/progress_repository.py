import json
import os
from src.core.entities.user_progress import UserProgress

PROGRESS_FILE = "user_progress.json"

class ProgressRepository:
    def load_progress(self) -> UserProgress:
        if not os.path.exists(PROGRESS_FILE):
            return UserProgress()
        
        try:
            with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                progress = UserProgress(
                    completed_lessons=set(data.get("completed_lessons", [])),
                    completed_exercises=set(data.get("completed_exercises", []))
                )
                return progress
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erro ao carregar progresso. Um novo será criado. Erro: {e}")
            return UserProgress()
        
    def save_progress(self, progress: UserProgress):
        try:
            data = {
                "completed_lessons": list(progress.completed_lessons),
                "completed_exercises": list(progress.completed_exercises)
            }
            with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Erro ao salvar progresso: {e}")