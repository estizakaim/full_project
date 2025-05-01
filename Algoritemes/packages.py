import cv2
from ultralytics import YOLO

# נתיב למודל המאומן
model_path = r"C:\Users\1\Desktop\full_project\Model\best.pt"  # עדכן את הנתיב שלך למודל
model = YOLO(model_path)  # טעינת המודל המאומן

# נתיב לתמונה
image_path = r"C:\Users\1\Desktop\full_project\Pictures\אנשים בתור3.jpg"  # עדכן את הנתיב שלך לתמונה

# קריאת התמונה
image = cv2.imread(image_path)

# הרצת המודל על התמונה
results = model(image)

# משתנה לספירת האנשים
people_count = 0

# עבור כל תוצאה (אם יש יותר מתוצאה אחת)
for result in results[0].boxes:  # results[0] מכיל את התוצאות של התמונה הנוכחית
    # קבלת קואורדינטות של התיבה: x1, y1, x2, y2
    x1, y1, x2, y2 = map(int, result.xyxy[0])  # גישה לקואורדינטות של התיבה

    # מזהה את הקלאס של האובייקט (אדם במודל YOLO)
    cls = int(result.cls[0])  # גישה לקלאס של האובייקט

    # אם הקלאס הוא 0 (אדם)
    if cls == 0:
        people_count += 1  # ספירת אנשים

        # ציור תיבה סביב האדם
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # ירוק עם קו בעובי 2

        # הוספת טקסט עם שם האובייקט
        cv2.putText(image, "Person", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# הדפסת מספר האנשים שנמצאו
print(f"Number of people detected: {people_count}")

# הצגת התמונה עם תיבות סביב האנשים
cv2.imshow("Detected People", image)
cv2.waitKey(0)  # חכה עד שמספיק ללחוץ על כפתור כדי לסגור
cv2.destroyAllWindows()  # סגור את כל החלונות שנפתחו
