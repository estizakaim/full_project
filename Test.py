import heapq

def dijkstra(graph, start_node):
    # אתחול מרחקים לאינסוף, והורה של כל קודקוד ל-None
    distances = {node: float('inf') for node in graph}
    parents = {node: None for node in graph}
    distances[start_node] = 0

    # תור עדיפויות לפי מרחקים
    priority_queue = [(0, start_node)]

    print(f"--- התחלת אלגוריתם מדייקסטרה מ-{start_node} ---")
    print(f"מצב התחלתי: distances = {distances}")
    print(f"-----------------------------")

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        print(f"\nנבחר קודקוד: {current_node} עם מרחק נוכחי: {current_distance}")

        # דילוג אם כבר מצאנו דרך קצרה יותר
        if current_distance > distances[current_node]:
            print("דילוג - כבר נמצא מסלול קצר יותר.")
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            print(f"  שוקלים שכן: {neighbor}, משקל קשת: {weight}, מרחק חדש מוצע: {distance}")

            if distance < distances[neighbor]:
                print(f"  ✔️ שיפור - מעדכנים מרחק של {neighbor} מ-{distances[neighbor]} ל-{distance}")
                distances[neighbor] = distance
                parents[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
            else:
                print(f"  ✖️ אין שיפור - לא מעדכנים את {neighbor}")

    print("\n--- סיום האלגוריתם ---")
    print("מרחקים סופיים:", distances)
    print("הורים:", parents)

    return distances, parents
