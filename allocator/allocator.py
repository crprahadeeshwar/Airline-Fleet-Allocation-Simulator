from models.assignment import Assignment
from Economics.calculators import calculate_costs, calculate_flight_time, calculate_revenue, calculate_net_profit, calculate_utilization

def greedy_feasibility_allocator(fleet, routes):

    feasibility_assignments = []

    for itinerary in routes:
        eligible_aircraft = []
        for aircraft in fleet:
            if aircraft.range >= itinerary.distance and aircraft.availableCount > 0 and aircraft.seats >= itinerary.demand:
                eligible_aircraft.append(aircraft)
        sorted_aircraft = sorted(eligible_aircraft, key=lambda x: x.seats)

        if sorted_aircraft:

            selected_Aircraft = sorted_aircraft[0]
            selected_Aircraft.availableCount -= 1
            assignment = Assignment(aircraft=selected_Aircraft, route=itinerary, ticketRevenue=0, operatingCostTotal=0, netProfit=0, flightTime=0, utilization=0)

        elif not eligible_aircraft:

            for aircraft in fleet:
                if aircraft.range >= itinerary.distance:
                    eligible_aircraft.append(aircraft)
            sorted_aircraft = sorted(eligible_aircraft, key=lambda x: x.seats, reverse=True)
            if sorted_aircraft:
                selected_Aircraft = sorted_aircraft[0]
                selected_Aircraft.availableCount -= 1
                assignment = Assignment(aircraft=selected_Aircraft, route=itinerary, ticketRevenue=0, operatingCostTotal=0, netProfit=0, flightTime=0, utilization=0)

        else:
            
            print(f"No suitable aircraft available for route from {itinerary.origin} to {itinerary.destination}.")
        feasibility_assignments.append(assignment)

        for assignment in feasibility_assignments:
            calculate_flight_time([assignment])
            calculate_costs([assignment])
            calculate_revenue([assignment])
            calculate_net_profit([assignment])
            calculate_utilization([assignment])


    return feasibility_assignments

 
def greedy_profit_allocator(fleet, routes):

    profit_assignments = []

    for itinerary in routes:
        eligible_aircraft = []
        profitable_aircraft = []
        for aircraft in fleet:
            if aircraft.range >= itinerary.distance and aircraft.availableCount > 0:
                eligible_aircraft.append(aircraft)

        for aircraft in eligible_aircraft:
            assignment = Assignment(aircraft=aircraft, route=itinerary, ticketRevenue=0, operatingCostTotal=0, netProfit=0, flightTime=0, utilization=0)
            calculate_flight_time([assignment])
            calculate_costs([assignment])
            calculate_revenue([assignment])
            calculate_net_profit([assignment])
            calculate_utilization([assignment])
            profitable_aircraft.append(assignment)

        sorted_profit_assignments = sorted(profitable_aircraft, key=lambda x: x.netProfit, reverse = True)

        if sorted_profit_assignments:
            selected_Assignment = sorted_profit_assignments[0]
            selected_Assignment.aircraft.availableCount -= 1
            profit_assignments.append(selected_Assignment)
        else:
            print(f"No suitable aircraft available for route from {itinerary.origin} to {itinerary.destination}.")


    return profit_assignments


def show_fleet_status(fleet):

    print("Fleet Status:")

    for aircraft in fleet:
        print(f"Aircraft: {aircraft.name}, Available Count: {aircraft.availableCount}")