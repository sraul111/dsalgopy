import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': [('B', 1), ('D', 4)],
    'B': [('C', 2), ('E', 3)],
    'C': [],
    'D': [('E', 1)],
    'E': []
}

# Find shortest paths from node 'A'
shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4, 'E': 4}
