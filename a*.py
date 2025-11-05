import heapq

def a_star_search(graph_data, costs, heuristic, start_node, goal_node):
    if start_node not in graph_data or goal_node not in graph_data:
        print("Error: Start or goal node not in graph.")
        return

    open_list = [(heuristic[start_node], start_node)]  
    
    g_cost = {node: float('inf') for node in graph_data}
    g_cost[start_node] = 0

    came_from = {}

    while open_list:
        f_current, current_node = heapq.heappop(open_list)

        if current_node == goal_node:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start_node)
            path.reverse()

            total_cost = g_cost[goal_node]
            print(f"\nA* Path Found: {' -> '.join(path)}")
            print(f"Total Cost: {total_cost}")
            return

        for neighbor in graph_data.get(current_node, []):
            edge_cost = costs.get((current_node, neighbor), float('inf'))
            temp_g_cost = g_cost[current_node] + edge_cost

            if temp_g_cost < g_cost[neighbor]:
                came_from[neighbor] = current_node
                g_cost[neighbor] = temp_g_cost
                
                f_cost = temp_g_cost + heuristic[neighbor]
                
                heapq.heappush(open_list, (f_cost, neighbor))

    print("\nA* Search failed: Goal node is unreachable.")

if __name__ == '__main__':
    graph = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['D', 'E'],
        'C': ['G'],
        'D': ['G'],
        'E': ['G'],
        'G': []
    }

    costs = {
        ('S', 'A'): 1, ('S', 'B'): 4,
        ('A', 'C'): 2, ('A', 'D'): 5,
        ('B', 'D'): 1, ('B', 'E'): 7,
        ('C', 'G'): 8,
        ('D', 'G'): 2,
        ('E', 'G'): 1
    }

    h_values = {
        'S': 10, 'A': 6, 'B': 4, 
        'C': 3, 'D': 2, 'E': 1, 'G': 0
    }
    
    a_star_search(graph, costs, h_values, 'S', 'G')