from dataclasses import dataclass

@dataclass
class Aircraft:
    name: str
    seats: int
    range: int
    availableCount: int
    fuelConsumption: float
    operatingCost: float
    speed: float
    def __post_init__(self):
        # Automatically rounds the float when the object is instantiated
        self.fuelConsumption = round(self.fuelConsumption, 2)
        self.operatingCost = round(self.operatingCost, 2)
        self.speed = round(self.speed, 2)
        