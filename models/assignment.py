from dataclasses import dataclass
from models.aircraft import Aircraft
from models.route import Route

@dataclass
class Assignment:
    aircraft: Aircraft
    route: Route
    ticketRevenue: float
    operatingCostTotal: float
    netProfit: float
    flightTime: float
    utilization: float 
    def __post_init__(self):
        # Automatically rounds the float when the object is instantiated
        self.utilization = round(self.utilization, 2)
        self.netProfit = round(self.netProfit, 2)
        self.operatingCostTotal = round(self.operatingCostTotal, 2)
        self.ticketRevenue = round(self.ticketRevenue, 2)
        self.flightTime = round(self.flightTime, 2)
        