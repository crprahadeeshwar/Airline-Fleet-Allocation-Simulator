from dataclasses import dataclass

@dataclass
class Route:
    origin: str
    destination: str
    distance: int
    demand: int
    ticketPrice: int
    