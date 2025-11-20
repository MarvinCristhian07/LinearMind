from src.infrastructure.content.lessons_data import LESSONS_CONTENT, LESSONS_ORDER
from src.infrastructure.content.exercises_data import EXERCISES_CONTENT, EXERCISES_ORDER
from src.core.entities.lesson import Lesson
from src.core.entities.exercise import Exercise
from typing import List, Dict, Optional

class GetContent:
    def get_lesson(self, lesson_id: str) -> Optional[Lesson]:
        return LESSONS_CONTENT.get(lesson_id)
    
    def get_all_lessons_in_order(self) -> List[Lesson]:
        return [LESSONS_CONTENT[lesson_id] for lesson_id in LESSONS_ORDER if lesson_id in LESSONS_CONTENT]
    
    def get_exercise(self, exercise_id: str) -> Optional[Exercise]:
        return EXERCISES_CONTENT.get(exercise_id)
    
    def get_exercise_by_level(self, level: str) -> List[Exercise]:
        if level not in EXERCISES_ORDER:
            return []
        
        exercise_ids = EXERCISES_ORDER[level]
        return [EXERCISES_CONTENT[ex_id] for ex_id in exercise_ids if ex_id in EXERCISES_CONTENT]