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

    def get_vertices(self):
        """
        מחזירה את כל מספרי המזהים של הקודקודים בגרף.
        """
        return list(self.adjacency_list.keys())

    def get_all_edges(self, vertex):
        """
        מחזירה את כל הקשתות שמחוברות לקודקוד נתון.
        """
        edges = []
        # עבור כל קשתות הגרף
        for edge in self.edges:  # נניח שself.edges הוא רשימה של קשתות, כל אחת מהם tuple של (from, to, weight)
            from_vertex, to_vertex, weight = edge  # שובר את ה-tuple לשדות נפרדים
            if from_vertex == vertex:
                edges.append((to_vertex, weight))  # אם הקודקוד מתאים, מוסיף את הקשת
            elif to_vertex == vertex:
                edges.append((from_vertex, weight))  # אם הקודקוד מתאים, מוסיף את הקשת גם מהכיוון השני
        return edges

    def get_vertex_data(self, vertex):
        """
        מחזירה את הנתונים הנלווים לקודקוד: שם מתקן, מיקומו, זמן המתנה, קיבולת
        """
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]["data"]  # מחזירה את הנתונים של הקודקוד
        return None

