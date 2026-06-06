from dataclasses import dataclass

@dataclass
class Aircraft:
    name: str
    seats: int
    range: int
    availableCount: int