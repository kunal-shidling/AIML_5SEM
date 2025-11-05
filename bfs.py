from collections import deque

def bfs_traversal(graph_data, start_node):
    if start_node not in graph_data:
        print(f"Error: Start node '{start_node}' not in graph.")
        return

    visited = {start_node}
    queue = deque([start_node])
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph_data.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print("\nBFS Traversal Order:")
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
    
    bfs_traversal(sample_graph, 'A')