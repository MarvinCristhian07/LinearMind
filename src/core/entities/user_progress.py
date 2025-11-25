from dataclasses import dataclass, field
from typing import Set

@dataclass
class UserProgress:
    completed_lessons: Set[str] = field(default_factory=set)
    completed_exercises: Set[str] = field(default_factory=set)

    def complete_lesson(self, lesson_id: str):
        self.completed_lessons.add(lesson_id)

    def complete_exercise(self, exercise_id: str):
        self.completed_exercises.add(exercise_id)

    def has_completed_lesson(self, lesson_id: str) -> bool:
        return lesson_id in self.completed_lessons
    
    def has_completed_exercise(self, exercise_id: str) -> bool:
        return exercise_id in self.completed_exercises