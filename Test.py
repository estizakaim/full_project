import cv2
from ultralytics import YOLO
import matplotlib.pyplot as plt
from packages import *

# טעינת המודל YOLOv11
model_path = r"C:\Users\1\Desktop\full_Project\Model\yolo11n.pt"
model = YOLO(model_path)


def detect_people_in_image(image_path, confidence_threshold=0.5):
    """ הפונקציה מקבלת כתובת של תמונה ומחזירה את מספר האנשים שזוהו בה """
    image = cv2.imread(image_path)  # קריאת התמונה
    if image is None:
        print("שגיאה בטעינת התמונה")
        return None

    # הרצת YOLO על התמונה
    results = model(image)

    people_count = 0  # ספירת האנשים בתמונה

    # מעבר על תוצאות הזיהוי
    for result in results:
        for box in result.boxes:
            confidence = box.conf[0]  # קבלת רמת האמינות של התוצאה
            cls = int(box.cls[0])  # זיהוי הקלאס של האובייקט

            if confidence >= confidence_threshold and cls == 0:  # YOLO מזהה "person" כ- class 0
                people_count += 1
                # צביעה של הבוקס על התמונה
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)

    print(f"מספר האנשים שזוהו בתמונה: {people_count}")

    # הצגת התמונה עם הבוקסות שסומנו
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

    return people_count


# קריאה לפונקציה עם התמונה הרצויה
image_path = r"C:\Users\1\Desktop\פרויקט לונה פארק\‏‏חומרים על מודלים\אנשים בתור\אנשים בתור5.jpg"
detect_people_in_image(image_path)
