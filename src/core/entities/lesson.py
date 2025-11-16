from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Slide:
    type: str
    content: Dict[str, str]

@dataclass
class Lesson:
    id: str
    title: str
    slides: List[Slide] = field(default_factory=list)