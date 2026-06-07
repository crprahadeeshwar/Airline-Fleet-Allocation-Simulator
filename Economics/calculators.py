
def calculate_flight_time(assignments):
    for assignment in assignments:
        route = assignment.route
        distance = route.distance
        aircraft = assignment.aircraft
        speed = aircraft.speed
        flight_time = distance / speed
        assignment.flightTime = flight_time

def calculate_costs(assignments):
    for assignment in assignments:
        total_cost = 0
        aircraft = assignment.aircraft
        route = assignment.route
        distance = route.distance
        fuel_cost = assignment.flightTime * aircraft.fuelConsumption * 1.1
        operating_cost = aircraft.operatingCost * assignment.flightTime
        total_cost += fuel_cost + operating_cost
        assignment.operatingCostTotal = total_cost

def calculate_revenue(assignments):
    for assignment in assignments:
        route = assignment.route
        ticket_revenue = route.demand * route.ticketPrice
        assignment.ticketRevenue = ticket_revenue

def calculate_net_profit(assignments):
    for assignment in assignments:
        net_profit = assignment.ticketRevenue - assignment.operatingCostTotal
        assignment.netProfit = net_profit

def calculate_utilization(assignments):
    for assignment in assignments:
        route = assignment.route
        aircraft = assignment.aircraft
        hours_flown = assignment.flightTime
        utilization = hours_flown / 24
        utilPercentage = utilization * 100
        assignment.utilization = utilPercentage

        