from Algoritemes.XML_Loader import get_video_paths,load_from_xml  # ייבוא מחלקת טעינת ה-XML
from Classes.Graph import Graph,print_graph  # מחלקת הגרף שמנהלת את הקודקודים והקשתות
from dijkstra import dijkstra  # ייבוא פונקציית דייקסטרה
from real_time import process_attractions

def process_user_selection(selected_names, graph):
    """
    הפונקציה מקבלת רשימת שמות מתקנים, ממירה אותם למזהים מתוך הגרף ומחזירה את זמני ההמתנה.
    """
    # יצירת סט כדי לאגור את המזהים של המתקנים שהמשתמש בחר
    selected_ids = set()

    # עבור על כל שם מתקן שהמשתמש בחר
    for name in selected_names:
        # חפש את ה-ID של המתקן לפי השם
        for vertex_id, data in graph.adjacency_list.items():
            if data["data"]["name"] == name:
                selected_ids.add(vertex_id)
                break  # יציאה מהלולאה לאחר שמצאנו את ה-ID


    # מחזירים את זמני המתנה
    return selected_ids


# יצירת גרף חדש על פי המחלקה Graph
graph = Graph()
# טעינת הנתונים לגרף
load_from_xml(graph, "C:/Users/1/Desktop/full_project/Data/park_data.xml")
#בדיקת תקינות
print_graph(graph)

# קריאה לפונקציה שממירה שמות של מתקנים למספר הID שלהם
selected_ids = process_user_selection(selected_names=["ספינת פיראטים", "קרוסלת מיני סירות","מגדלי הכח","כוכב"], graph=graph)  # דוגמה של קריאה עם שמות

# קבלת נתיבי הווידאו עבור המתקנים שנבחרו
video_paths =get_video_paths(graph,selected_ids)  # selected_ids היא רשימת מזהים

# חישוב זמני המתנה עבור המתקנים
wait_times = process_attractions(selected_ids, video_paths)

# שליפת המפתח הראשון מהמילון (ה-ID הראשון)
first_key = list(wait_times.keys())[0]

# קריאה לפונקציית דייקסטרה עם הגרף והקודקוד הראשון
dijkstra(graph, first_key)
