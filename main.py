from data.loader import load_fleet, load_routes
from allocator.allocator import allocate_aircraft_to_routes, show_fleet_status
fleet = load_fleet("data/fleet.csv")
routes = load_routes("data/routes.csv")

assignments = allocate_aircraft_to_routes(fleet, routes)
print("Aircraft assigned to routes:")
for assignment in assignments:
    print(f"Route: {assignment.route.origin} to {assignment.route.destination}, Aircraft: {assignment.aircraft.name}")
show_fleet_status(fleet)