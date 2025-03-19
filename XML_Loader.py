from packages import *

class XML_Loader:
    def __init__(self, graph):
        """
        מאתחלת את המחלקה עם גרף, שיתמלא בנתונים מקובץ ה-XML
        """
        self.graph = graph

    def load_from_xml(self, file_path):
        """
        טוענת נתונים מקובץ XML ומבנה את הגרף.
        """
        tree = ET.parse(file_path)  # קריאת קובץ ה-XML ויצירת עץ
        root = tree.getroot()  # קבלת השורש של העץ

        # קריאת הקודקודים מתוך קובץ ה-XML
        for attraction in root.findall('.//attraction'):
            # קריאה של כל המידע עבור כל אטרקציה
            attraction_id = int(attraction.find('id').text)  # מזהה הקודקוד
            name = attraction.find('name').text  # שם האטרקציה
            capacity = int(attraction.find('capacity').text)  # קיבולת
            wait_time = int(attraction.find('wait_time').text)  # זמן המתנה

            # הוספת הקודקוד לגרף עם כל המידע
            self.graph.add_vertex(attraction_id, {"name": name, "capacity": capacity, "wait_time": wait_time})

        # קריאת הקשתות מתוך קובץ ה-XML
        for edge in root.findall('.//edge'):
            from_attraction = int(edge.find('from').text)  # מזהה הקודקוד שממנו יוצאת הקשת
            to_attraction = int(edge.find('to').text)  # מזהה הקודקוד שאליו נכנסת הקשת
            weight = int(edge.find('weight').text)  # משקל הקשת (המרחק)

            # הוספת הקשת לגרף
            self.graph.add_edge(from_attraction, to_attraction, weight)

    def get_video_paths(self, attraction_ids):
        """ מחזיר רשימה של נתיבי סרטונים עבור רשימה של מזהי מתקנים. """
        video_paths = {}  # מילון לשמירת נתיבי הסרטונים
        for attraction_id in attraction_ids:
            video_path = self.video_paths.get(attraction_id)
            if video_path:  # אם יש נתיב סרטון
                video_paths[attraction_id] = video_path
        return video_paths
