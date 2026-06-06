from models.assignment import Assignment


def allocate_aircraft_to_routes(fleet, routes):
    assignments = []
    for itinerary in routes:
        eligible_aircraft = []
        for aircraft in fleet:
            if aircraft.range >= itinerary.distance and aircraft.availableCount > 0 and aircraft.seats >= itinerary.demand:
                eligible_aircraft.append(aircraft)
        sorted_aircraft = sorted(eligible_aircraft, key=lambda x: x.seats)
        if sorted_aircraft:
            selected_Aircraft = sorted_aircraft[0]
            selected_Aircraft.availableCount -= 1
            assignment = Assignment(selected_Aircraft, itinerary)
        elif not eligible_aircraft:
            for aircraft in fleet:
                if aircraft.range >= itinerary.distance:
                    eligible_aircraft.append(aircraft)
            sorted_aircraft = sorted(eligible_aircraft, key=lambda x: x.seats, reverse=True)
            if sorted_aircraft:
                selected_Aircraft = sorted_aircraft[0]
                selected_Aircraft.availableCount -= 1
                assignment = Assignment(selected_Aircraft, itinerary)
        else:
            print(f"No suitable aircraft available for route from {itinerary.origin} to {itinerary.destination}.")
        assignments.append(assignment)
    return assignments

def show_fleet_status(fleet):
    print("Fleet Status:")
    for aircraft in fleet:
        print(f"Aircraft: {aircraft.name}, Available Count: {aircraft.availableCount}")