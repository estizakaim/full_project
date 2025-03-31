import heapq #מבנה נתונים של תור עדיפות- מימוש בערימת מינימום


def dijkstra(graph, start): #מקבלת גרף ונקודת התחלה
    # יצירת תור עדיפויות ואתחול בנקודת ההתחלה
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    # אתחול מרחקים עד אינסוף ואת הראשון ל-0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # אתחול מסלולים קודמים
    previous_nodes = {node: None for node in graph}

#לולאה ראשית שמתבצעת כל עוד יש קודקודים בתור שלוף את הצומת עם המרחק הקצר
    while priority_queue:
        #תכניס למשתנה הראשון את המרחק של הקודקוד המיניצלי ולמשתנה השני את הקודקוד
        current_distance, current_node = heapq.heappop(priority_queue)

        # אם המרחק שנשלף גדול יותר מזה שמעודכן במילון המרחקים, אפשר לדלג כי יש בידנו את המינימום
        if current_distance > distances[current_node]:
            continue
        # אחרת עבור אותו צומת בדוק את השכנים שלו
        for neighbor, weight in graph[current_node].items():
            #נכניס למשתנה את המרחק שצברנו עד עכשיו פלוס המרחק ממני לשכן
            distance = current_distance + weight

            # אם המרחק שנמצא קטן ממה שקיים במילון המרחקים- אם נמצא מסלול קצר יותר, מעדכנים
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes


# דוגמה לשימוש
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)
print("מרחקים מהנקודה ההתחלתית:", distances)
print("מסלולים קודמים:", previous_nodes)
