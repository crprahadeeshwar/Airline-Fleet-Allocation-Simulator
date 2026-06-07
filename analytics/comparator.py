from allocator.allocator import greedy_profit_allocator, greedy_feasibility_allocator

def compare_allocators(fleet, routes):
    print("Comparing Greedy Feasibility and Profit Allocators:")
    feasibility_assignments = greedy_feasibility_allocator(fleet, routes)
    profit_assignments = greedy_profit_allocator(fleet, routes)
    total_profit_feasibility = sum(assignment.netProfit for assignment in feasibility_assignments)
    total_profit_profit = sum(assignment.netProfit for assignment in profit_assignments)
    print(f"Total Profit from Greedy Feasibility Allocator: ${total_profit_feasibility}")
    print(f"Total Profit from Greedy Profit Allocator: ${total_profit_profit}")
    if total_profit_profit > total_profit_feasibility:
        print("Greedy Profit Allocator is more profitable.")
    elif total_profit_feasibility > total_profit_profit:
        print("Greedy Feasibility Allocator is more profitable.")
    else:
        print("Both allocators have the same total profit.")
    average_utilization_feasibility = sum(assignment.utilization for assignment in feasibility_assignments) / len(feasibility_assignments)
    average_utilization_profit = sum(assignment.utilization for assignment in profit_assignments) / len(profit_assignments)
    print(f"Average Utilization from Greedy Feasibility Allocator: {average_utilization_feasibility}%")
    print(f"Average Utilization from Greedy Profit Allocator: {average_utilization_profit}%")
    if average_utilization_profit > average_utilization_feasibility:
        print("Greedy Profit Allocator has higher average utilization.")
    elif average_utilization_feasibility > average_utilization_profit:
        print("Greedy Feasibility Allocator has higher average utilization.")
    else:
        print("Both allocators have the same average utilization.")
    




