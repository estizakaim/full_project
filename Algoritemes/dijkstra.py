import heapq

def dijkstra(graph, start_node):
    print(graph)
    # אתחול מרחקים לאינסוף, והורה של כל קודקוד ל-None
    distances = {node: float('inf') for node in graph}
    parents = {node: None for node in graph}
    distances[start_node] = 0

    # תור עדיפויות לפי מרחקים
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # דילוג אם כבר מצאנו דרך קצרה יותר
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, parents
