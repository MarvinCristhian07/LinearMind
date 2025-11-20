from src.infrastructure.services.gemini_service import GeminiService
from src.core.entities.exercise import Exercise
from typing import Dict, Any

class GetAIHint:
    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    def execute(self, exercise: Exercise, user_answers: Dict[str, Any]) -> str:
        return self.gemini_service.get_ai_hint(
            exercise_prompt=exercise.prompt,
            correct_answers=exercise.answers,
            user_answers=user_answers,
            ai_context=exercise.ai_context
        )