import heapq

def dijkstra(graph, start, end=None):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    if end:
        path = []
        current_node = end
        while current_node is not None:
            path.append(current_node)
            current_node = previous_nodes[current_node]
        path.reverse()
        return distances[end], path
    else:
        return distances

graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'D': 2},
    'C': {'B': 1, 'D': 1},
    'D': {}
}
start_node = 'A'
end_node = 'D'

shortest_distance, shortest_path = dijkstra(graph, start_node, end_node)
print("Distancia más corta desde el nodo", start_node, "al nodo", end_node, ":", shortest_distance)
print("Ruta más corta:", shortest_path)

shortest_distances = dijkstra(graph, start_node)
print("Distancias más cortas desde el nodo", start_node, ":", shortest_distances)