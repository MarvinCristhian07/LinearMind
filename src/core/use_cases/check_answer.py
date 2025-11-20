import math
from typing import Dict, Any, Tuple

class CheckAnswer:
    def execute(self, user_answers: Dict[str, Any], correct_answers: Dict[str, Any]) -> Tuple[bool, Dict[str, bool]]:
        is_fully_correct = True
        field_results = {}

        for key, correct_val in correct_answers.items():
            if key not in user_answers:
                is_fully_correct = False
                field_results[key] = False
                continue

            user_val = user_answers.get(key)
            is_field_correct = False

            # Lógica de comparação
            try:
                if isinstance(correct_val, (float, int)):
                    user_val_float = float(user_val)
                    is_field_correct = math.isclose(user_val_float, float(correct_val), rel_tol=1e-5)
                else:
                    is_field_correct = str(user_val).strip().lower() == str(correct_val).strip().lower()

            except (ValueError, TypeError):
                is_field_correct = False

            field_results[key] = is_field_correct

            if not is_field_correct:
                is_fully_correct = False

        return is_fully_correct, field_results