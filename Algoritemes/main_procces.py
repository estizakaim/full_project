from Algoritemes.XML_Loader import XML_Loader  # ייבוא מחלקת טעינת ה-XML
from Classes.Graph import Graph  # נניח שזו המחלקה שמנהלת את הגרף


def process_user_selection(selected_names, graph):
    graph = Graph()
    xml_loader = XML_Loader(graph)  # יצירת אובייקט מסוג XML_Loader
    xml_loader.load_from_xml("park_data.xml")  # טעינת הנתונים לגרף
    """
    ממירה רשימת שמות מתקנים לרשימת מזהים ומחזירה אותם.
    אם השם לא נמצא בגרף, הוא לא ייכלל ברשימה.
    """
    selected_ids = set()

    # עבור על כל שם של מתקן שהמשתמש בחר
    for name in selected_names:
        # חפש את ה-ID של המתקן לפי השם
        for vertex_id, data in graph.adjacency_list.items():
            if data["data"]["name"] == name:
                selected_ids.add(vertex_id)
                break  # יציאה מהלולאה ברגע שמצאנו את ה-ID
    video_paths = xml_loader.get_video_paths(selected_ids)  # selected_ids זו רשימת מזהים
    return process_attractions(selected_ids, video_paths)
