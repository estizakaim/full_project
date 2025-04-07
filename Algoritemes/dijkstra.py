import heapq  # מבנה הנתונים heap- ערימת מינימום מאפשר להשתמש כבסיס לתור קדימויות


# שורה 1: אתחול האומדנים
def dijkstra(graph, start):
    # P - עץ המסלולים, D - האומדן (המרחקים)
    D = {node: float('inf') for node in graph}  # כל הקודקודים מתחילים עם ערך אינסופי
    D[start] = 0  # המרחק מהקודקוד ההתחלתי הוא 0
    P = {node: None for node in graph}  # האב של כל קודקוד (בהתחלה כל האבות הם None)

    S = set()  # קבוצת הקודקודים שסיימנו לחשב את המסלול הקצר ביותר עבורם וביצענו הקלה על שכניו

    # שורה 3-4: אתחול תור קדימויות Q
    Q = [(0, start)]  # תור Q הוא למעשה רשימה של זוגות, כשהמפתח (או העדיפות) הוא הערך הראשון בזוג והאובייקט הוא הערך השני
    #תחילה מכיל את הקודקוד ההתחלתי
    heapq.heapify(Q)  # הופך את Q לתור קדימויות

    while Q:  # שורות 5-7: כל עוד ישנם קודקודים בתור
#שליפת הקודקוד עם המרחק הקטן ביותר בכל פעם מבטיחה שמצאנו את המסלול הקצר ביותר אליו,
# ומעבר דרך הקודקוד הזה מבטיח שמסלול הקצר ביותר יעודכן לשכניו
        current_distance, u = heapq.heappop(Q)
        S.add(u)  # הוספת הקודקוד S

        # עבור כל קשת היוצאת מ-U
        for v, weight in graph[u]:
            if v not in S:  # אם v לא נמצא בקבוצת S
                distance = current_distance + weight  # חישוב המרחק החדש דרך הקשת (u, v)
                # אם המרחק החדש קטן יותר מהאומדן הקודם
                if distance < D[v]:
                    D[v] = distance  # עדכון האומדן של v
                    P[v] = u  # עדכון האב של v
                    heapq.heappush(Q, (D[v], v))  # הוספת הקודקוד לתור הקדימויות
    return D, P


# פונקציה לשחזור המסלול הקצר ביותר
def reconstruct_path(P, start, end):
    path = []
    current_node = end
    while current_node is not None:
        path.append(current_node)
        current_node = P[current_node]
    path.reverse()  # הפוך את המסלול כדי להתחיל מהקודקוד ההתחלתי
    return path


# דוגמה לשימוש
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
distances, parents = dijkstra(graph, start_node)

print("מרחקים מקודקוד התחלה:", distances)
print("אבות עבור כל קודקוד:", parents)

# הדפסת המסלול הקצר ביותר לכל קודקוד
for node in graph:
    if node != start_node:
        path = reconstruct_path(parents, start_node, node)
        print(f"המסלול הקצר ביותר מ-{start_node} ל-{node}: {path}")
