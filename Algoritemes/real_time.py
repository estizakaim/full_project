import cv2  # כלי לעיבוד תמונה
import time  # ספריה לעבודה עם זמן כדי לדעת מתי עוברים 5 שניות
from ultralytics import YOLO  # מודל לזיהוי אובייקטים בתמונה

# נסה לטעון את המודל
model_path = r"/Model/yolo11n.pt"  # ניתוב לקובץ המכיל את המודל המאומן לזיהוי אובייקטים
model = YOLO(model_path)  # בניית אובייקט מסוג YOLO שיכול לזהות אובייקטים בתמונה

def detect_people_5s(video_path):
    """ הפונקציה מקבלת כקלט את הסרטון, מזהה אנשים ומחזירה את מספר האנשים לאחר 5 שניות. """
    cap = cv2.VideoCapture(video_path)  # פתיחת סרטון באמצעות OpenCV והמשתנה cap יכיל את אובייקט הסרטון שנוצר

    start_time = None  # משתנה לשמירת הזמן שבו זוהה אדם לראשונה
    detected_people = 0  # משתנה לשמירת מספר האנשים שזוהו ע"פ הממוצע הסופי שנמצא
    frame_count=0 # משתנה הסופר את מספר הפריימים
    while cap.isOpened():  # לולאה שפועלת כל עוד הסרטון פתוח
        frame_count+=1
        ret, frame = cap.read()  # קריאת הפריים הבא בסרטון
        if not ret:  # אם הפריים לא תקין - צא מהלולאה
            break

        results = model(frame)  # הרצת YOLO על הפריים הנוכחי
        people_count = 0  # ספירת האנשים בפריים
        for result in results:  # ריצה על אובייקטים שנמצאו בפריים הנוכחי
            for box in result.boxes:  # ריצה על התיבות שנמצאו באובייקט
                cls = int(box.cls[0])  # מזהה את הקלאס של האובייקט
                if cls == 0:  # YOLO מזהה "person" כ- class 0
                    people_count += 1  # ספירת האנשים שזוהו
        detected_people+=people_count
        if people_count > 0:  # אם זוהה לפחות אדם אחד
            if start_time is None:  # אם זו הפעם הראשונה שזוהה אדם, נתחיל למדוד זמן
                start_time = time.time()  # שמירת הזמן הנוכחי

            elapsed_time = time.time() - start_time  # מחשב כמה זמן עבר מאז הזיהוי הראשון

            if elapsed_time >= 5:  # אם עברו 5 שניות מאז הזיהוי הראשון
                detected_people =detected_people/frame_count
  # שמירת מספר האנשים שזוהו בפריים לאחר 5 שניות
                print("Captured frame after 5 seconds and saved as 'detected_frame_after_5_seconds.jpg'")
                print(f"People count in saved frame: {detected_people}")  # הדפסת מספר האנשים שזוהו בפריים שנשמר
                break  # עצירת הלולאה לאחר סיום הספירה

    cap.release()  # סגירת החלונות שנפתחו עם האובייקט שיצרנו cv2.VideoCapture()
    cv2.destroyAllWindows()  # סגירת כל החלונות שנפתחו
    return detected_people  # החזרת מספר האנשים שזוהו


def calculate_wait_time(attractions, attraction_id, people_in_queue):
    """ הפונקציה מקבלת את מספר האנשים בתור ומחשבת את זמן ההמתנה לפי הקיבולת של המתקן. """
    if attraction_id not in attractions:  # אם המתקן לא קיים במערכת
        raise ValueError(f"מתקן עם ID {attraction_id} לא נמצא במערכת")

    attraction = attractions[attraction_id]  # שליפת המידע על המתקן
    capacity = attraction['capacity']  # קיבולת המתקן
    wait_time = attraction['wait_time']  # זמן פעולה למתקן

    cycles_needed = -(-people_in_queue // capacity)  # חישוב ceiling לחלוקה (מספר מחזורי עבודה)
    total_wait_time = cycles_needed * wait_time  # חישוב זמן ההמתנה הכולל

    return total_wait_time


def process_attractions(attractions,video_paths):
    """ הפונקציה מקבלת את המתקנים ואת נתיבי הסרטונים, ומחשבת את זמן ההמתנה לכל מתקן. """
    wait_times = {}  # מילון לשמירת זמני ההמתנה לכל מתקן

    for attraction_id, attraction in attractions.items():  # עבור כל מתקן במערכת
        if attraction_id not in video_paths:  # אם לא נמצא נתיב סרטון עבור מתקן זה
            raise ValueError(f"לא נמצא קובץ וידאו למתקן עם ID {attraction_id}")

        # חישוב מספר האנשים בתור בעזרת הפונקציה detect_people_5s
        people_in_queue = detect_people_5s(video_paths[attraction_id])

        # חישוב זמן ההמתנה עבור כל מתקן
        total_wait_time = calculate_wait_time(attractions, attraction_id, people_in_queue)

        # שמירה של זמן ההמתנה עבור כל מתקן
        wait_times[attraction_id] = total_wait_time

    return wait_times  # החזרת מילון של זמני ההמתנה לכל המתקנים
