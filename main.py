from analytics.comparator import compare_allocators
from data.loader import load_fleet, load_routes
from allocator.allocator import greedy_feasibility_allocator, greedy_profit_allocator, show_fleet_status
from Economics.calculators import calculate_costs, calculate_flight_time, calculate_revenue, calculate_net_profit, calculate_utilization


def run_profit_allocator():

    fleet = load_fleet("data/fleet.csv")
    routes = load_routes("data/routes.csv")

    assignments = greedy_profit_allocator(fleet, routes)

    print("Aircraft assigned to routes based on profit successfully.")

    show_fleet_status(fleet)
    calculate_flight_time(assignments)
    calculate_costs(assignments)
    calculate_revenue(assignments)
    calculate_net_profit(assignments)
    calculate_utilization(assignments)

    for assignment in assignments:
        print(f"Route: {assignment.route.origin} to {assignment.route.destination}, Aircraft: {assignment.aircraft.name}, Ticket Revenue: ${assignment.ticketRevenue}, Operating Cost: ${assignment.operatingCostTotal}, Net Profit: ${assignment.netProfit}, Flight Time: {assignment.flightTime}, Utilization: {assignment.utilization}%")

def run_feasibility_allocator():
    
    fleet = load_fleet("data/fleet.csv")
    routes = load_routes("data/routes.csv")

    assignments = greedy_feasibility_allocator(fleet, routes)

    print("Aircraft assigned to routes based on feasibility successfully.")

    show_fleet_status(fleet)
    calculate_flight_time(assignments)
    calculate_costs(assignments)
    calculate_revenue(assignments)
    calculate_net_profit(assignments)
    calculate_utilization(assignments)

    for assignment in assignments:
        print(f"Route: {assignment.route.origin} to {assignment.route.destination}, Aircraft: {assignment.aircraft.name}, Ticket Revenue: ${assignment.ticketRevenue}, Operating Cost: ${assignment.operatingCostTotal}, Net Profit: ${assignment.netProfit}, Flight Time: {assignment.flightTime}, Utilization: {assignment.utilization}%")

def run_comparator():
    
    fleet = load_fleet("data/fleet.csv")
    routes = load_routes("data/routes.csv")

    compare_allocators(fleet, routes)

def main():

    print("\n" + "="*50 + "\n")

    print("Running Profit Allocator:")
    run_profit_allocator()
    print("\n" + "="*50 + "\n")

    print("Running Feasibility Allocator:")
    run_feasibility_allocator()
    print("\n" + "="*50 + "\n")

    print("Comparing Allocators:")
    run_comparator()
    print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()

