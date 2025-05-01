import xml.etree.ElementTree as ET

def load_from_xml(graph, file_path):
    """
    טוענת נתונים מקובץ XML ובונה את הגרף.
    """
    tree = ET.parse(file_path)  # קריאת קובץ ה-XML ויצירת עץ
    root = tree.getroot()  # קבלת השורש של העץ

    # קריאת הקודקודים (attractions) מתוך קובץ ה-XML
    for attraction in root.findall('.//attraction'):
        # קריאה של כל המידע עבור כל אטרקציה
        attraction_id = int(attraction.find('id').text)  # מזהה הקודקוד
        name = attraction.find('name').text  # שם האטרקציה
        capacity = int(attraction.find('capacity').text)  # קיבולת
        wait_time = int(attraction.find('wait_time').text)  # זמן המתנה
        location_elem = attraction.find('location')  # מיקום (אם קיים)
        location = location_elem.text if location_elem is not None else "unknown"

        # הוספת הקודקוד לגרף עם כל המידע
        graph.add_vertex(attraction_id, {
            "name": name,
            "capacity": capacity,
            "wait_time": wait_time,
            "location": location
        })

    # קריאת הקשתות (edges) מתוך קובץ ה-XML
    edges_element = root.find("edges")
    if edges_element is not None:
        for edge in edges_element.findall('edge'):
            from_attraction = int(edge.find('from').text)
            to_attraction = int(edge.find('to').text)
            weight = int(edge.find('weight').text)

            # הוספת הקשת רק אם עדיין לא קיימת
            if not graph.has_edge(from_attraction, to_attraction):
                graph.add_edge(from_attraction, to_attraction, weight)

    # קריאת הסרטונים (videos) מתוך קובץ ה-XML
    graph.videos = {}

    for video in root.findall('.//video'):
        attraction_id = int(video.find('attraction_id').text)
        path = video.find('path').text

        if attraction_id not in graph.videos:
            graph.videos[attraction_id] = []
        graph.videos[attraction_id].append(path)

    print("נתונים נטענו בהצלחה.")

def get_video_paths(graph, attraction_ids):
    """ מחזיר מילון של מזהה -> נתיב לסרטון (מחרוזת, לא רשימה). """
    video_paths = {}

    for attraction_id in attraction_ids:
        if attraction_id in graph.videos and graph.videos[attraction_id]:
            video_paths[attraction_id] = graph.videos[attraction_id][0]

    return video_paths
