import sys
import os
from packages import *
from Real_time import detect_people_5s
from XML_Loader import XML_Loader  # ייבוא מחלקת טעינת ה-XML
from my_graph import Graph  # נניח שזו המחלקה שמנהלת את הגרף
#vvvvvvvvvvvvvvvvvv
if __name__ == "__main__":
    # יצירת גרף
    graph = Graph()

    # טעינת הנתונים מקובץ XML
    xml_loader = XML_Loader(graph)  # יצירת אובייקט מסוג XML_Loader
    xml_loader.load_from_xml("park_data.xml")  # טעינת הנתונים לגרף


    def process_user_selection(selected_names, graph):
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
        return process_attractions (selected_ids,video_paths)


    # עכשיו הגרף מוכן עם כל המידע, אפשר להתחיל בזיהוי אנשים
    video_path = r"C:\Users\1\Desktop\full_Project\video\video.mp4"
    unique_people_count = detect_people_5s(video_path)
    print(f"Total unique people counted: {unique_people_count}")

    # דוגמה לזיהוי אנשים עם המתנה של 5 שניות
    detect_people_5s(video_path)
