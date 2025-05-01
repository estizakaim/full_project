import cv2  # כלי לעיבוד תמונה
from ultralytics import YOLO  # מודל לזיהוי אובייקטים בתמונה
import os
# פונקציית עזר להצגת תיבות על תמונה
def display_image_with_boxes(image, boxes):
    """
    מציגה תמונה עם תיבות סביב אובייקטים שמחלקתם 0 ("person").
    """
    for box in boxes:
        if int(box.cls[0]) == 0:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, "Person", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detected People", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




# פונקציה לספירת אנשים בתמונות
def count_people_in_images(video_paths):
    """
     מקבלת מילון של: מזהה -> ניתוב תמונה
 מחזירה מילון של: מזהה -> מספר אנשים
    """
    if not video_paths:
        raise ValueError("יש לספק מילון לא ריק של נתיבי תמונות.")  # בודקת אם המילון ריק

    model = YOLO(r"C:\Users\1\Desktop\full_project\Model\yolov8n.pt")  # טוען את מודל YOLO לזיהוי אובייקטים
    results = {}  # יצירת מילון שיכיל את התוצאות (מזהה -> מספר אנשים)

    # עבור כל מזהה תמונה ונתיב שלה במילון
    for attraction_id, image_path in video_paths.items():
        image = cv2.imread(image_path)  # קורא את התמונה מהנתיב
        if image is None:  # בודקת אם התמונה לא נטענה כראוי
            print(f"אזהרה: לא ניתן לקרוא את התמונה – {image_path}")
            continue  # ממשיכה לתמונה הבאה
        result = model(image)[0]  # מפעילה את המודל על התמונה ומקבלת את התוצאות (האובייקטים שזוהו)
        people_count = sum(1 for box in result.boxes if int(box.cls[0]) == 0)  # סופרת את מספר האנשים (קטגוריה 0)
        results[attraction_id] = people_count  # שומרת את מספר האנשים עבור המתקן הנוכחי במילון
        #display_image_with_boxes(image, result.boxes)  # מציגה את התמונה עם התיבות שסימנו את האנשים
    return results  # מחזירה את המילון שמכיל את מספר האנשים לכל מזהה



# חישוב זמן המתנה למתקנים
def wait_time(people_counts):
        """
        מקבלת מילון: מזהה -> מספר אנשים,
        מחזירה מילון: מזהה -> זמן המתנה.
        """
        from main_procces import graph
        wait_times = {}  # מילון חדש לשמירת זמני ההמתנה לכל מתקן

        for attraction_id, people_in_queue in people_counts.items():  # מעבר על כל מתקן וכמות האנשים שזוהו בו
            data = graph.get_vertex_data(attraction_id)
            capacity = data['capacity']  # קיבולת של המתקן – כמה אנשים נכנסים במחזור אחד
            wait_time = data['wait_time']  # זמן פעולה של המתקן (משך מחזור אחד)

            # חישוב כמה מחזורים דרושים כדי להכניס את כל האנשים (ceil בלי math)
            # אם אין אנשים – זמן ההמתנה הוא אפס
            cycles_needed = -(-people_in_queue // capacity) if people_in_queue else 0

            # שמירה של זמן ההמתנה הכולל במילון לפי מזהה המתקן
            wait_times[attraction_id] = cycles_needed * wait_time

        return wait_times  # מחזיר את המילון עם זמני ההמתנה לכל מתקן


# פונקציה ראשית לחישוב זמני המתנה
def process_attractions(image_paths):
    """
    הפונקציה מקבלת את המתקנים ואת נתיבי התמונות, ומחשבת את זמן ההמתנה לכל מתקן.
    """
    wait_times = {}

    #קריאה לפונקציית ספירת אנשים בתמונה
    people_counts = count_people_in_images(image_paths)

    wait_times = wait_time(people_counts)

    return wait_times
