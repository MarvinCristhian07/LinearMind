from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class Exercise:
    id: str
    level: str
    prompt: str
    inputs: Dict[str, str]
    answers: Dict[str, Any]
    ai_context: str = ""
    image_path: Optional[str] = None