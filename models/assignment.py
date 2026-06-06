from dataclasses import dataclass
from models.aircraft import Aircraft
from models.route import Route

@dataclass
class Assignment:
    aircraft: Aircraft
    route: Route