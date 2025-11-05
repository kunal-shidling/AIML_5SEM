def dfs_traversal(graph_data, start_node):
    if start_node not in graph_data:
        print(f"Error: Start node '{start_node}' not in graph.")
        return

    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)

            for neighbor in reversed(graph_data.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    print("\nDFS Traversal Order:")
    print(" -> ".join(map(str, traversal_order)))

if __name__ == '__main__':
    sample_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    dfs_traversal(sample_graph, 'A')