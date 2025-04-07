class Graph:
    def __init__(self):
        """
        מאתחלת את הגרף עם רשימת סמיכויות ריקה
        """
        self.adjacency_list = {}  # מבנה נתונים של מילון

    def add_vertex(self, vertex, data=None):
        """
        יצירת קודקוד המורכב ממערך קשתות של הקודקוד והכנסת הדאטה שלו
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {"edges": [], "data": data}  # הוספת קודקוד עם קשתות ריקות

    def add_edge(self, vertex1, vertex2, weight=1):
        """
        הוספת קשת בין שני קודקודים לגרף עם משקל קודם בודק שהקודקוד קיים
        יוצר קשת ל2 הכיוונים כי הגרף לא מכוון
        """
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1]["edges"].append((vertex2, weight))
            self.adjacency_list[vertex2]["edges"].append((vertex1, weight))  # עבור גרף לא מכוון

    def get_all_edges(self, vertex):
        """
        מחזירה את כל הקשתות שמחוברות לקודקוד נתון.
        """
        edges = []
        for to_vertex, weight in self.adjacency_list[vertex]["edges"]:
            edges.append((to_vertex, weight))  # מחזיר את כל הקשתות שנכנסות או יוצאות מהקודקוד
        return edges

    def get_vertices(self):
        """
        מחזירה את כל מספרי המזהים של הקודקודים בגרף.
        """
        return list(self.adjacency_list.keys())

    def get_vertex_data(self, vertex):
        """
        מחזירה את הנתונים הנלווים לקודקוד: שם מתקן, מיקומו, זמן המתנה, קיבולת
        """
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]["data"]  # מחזירה את הנתונים של הקודקוד
        return None


# הפונקציה המדפיסה את הגרף כולל קשתות בצורה של XML
def print_graph(graph):
    # הדפסת קודקודים
    print("קודקודים בגרף:")
    for vertex in graph.get_vertices():
        data = graph.get_vertex_data(vertex)
        if data:
            print(f"ID: {vertex}, Name: {data['name']}, Capacity: {data['capacity']}, Wait Time: {data['wait_time']}")
        else:
            print(f"ID: {vertex}, No data found")

    # הדפסת קשתות
    print("\nקשתות בגרף:")
    print("<edges>")  # הדפסת התג <edges> שמתחיל את בלוק הקשתות
    for vertex in graph.get_vertices():
        edges = graph.get_all_edges(vertex)
        for edge in edges:
            to_vertex, weight = edge
            print(f"  <edge>")
            print(f"    <from>{vertex}</from>")
            print(f"    <to>{to_vertex}</to>")
            print(f"    <weight>{weight}</weight>")
            print(f"  </edge>")
    print("</edges>")  # הדפסת התג </edges> שמסיים את בלוק הקשתות
