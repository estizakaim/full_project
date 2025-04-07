from Algoritemes.packages import *
import cv2
import matplotlib.pyplot as plt
from Algoritemes.XML_Loader import get_video_paths,load_from_xml  # ייבוא מחלקת טעינת ה-XML
from Classes.Graph import Graph  # מחלקת הגרף שמנהלת את הקודקודים והקשתות

# # טעינת המודל YOLOv11
# model_path = r"C:\Users\1\Desktop\full_Project\Model\yolo11n.pt"
# model = YOLO(model_path)

# # פונקציה לבדיקת חשיכה בתמונה
# def is_dark_image(image):
#     """בודקת אם התמונה חשוכה על בסיס ממוצע בהירות התמונה"""
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     avg_brightness = gray.mean()
#     return avg_brightness < 50  # אם ממוצע הבהירות נמוך מ-50, התמונה חשוכה
#
# # פונקציה להבהרת התמונה
# def brighten_image(image):
#     """מבצע הבהרה לתמונה"""
#     hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#     hsv[:, :, 2] = cv2.normalize(hsv[:, :, 2], None, 0, 255, cv2.NORM_MINMAX)
#     return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
#
# def detect_people_in_image(image_path, confidence_threshold=0.5):
#     """ הפונקציה מקבלת כתובת של תמונה ומחזירה את מספר האנשים שזוהו בה """
#     image = cv2.imread(image_path)  # קריאת התמונה
#     if image is None:
#         print("שגיאה בטעינת התמונה")
#         return None
#
#     # אם התמונה חשוכה, מבצעים הבהרה
#     if is_dark_image(image):
#         print("התמונה חשוכה, מבצע הבהרה")
#         image = brighten_image(image)
#
#     # הרצת YOLO על התמונה
#     results = model(image)
#
#     people_count = 0  # ספירת האנשים בתמונה
#
#     # מעבר על תוצאות הזיהוי
#     for result in results:
#         for box in result.boxes:
#             confidence = box.conf[0]  # קבלת רמת האמינות של התוצאה
#             cls = int(box.cls[0])  # זיהוי הקלאס של האובייקט
#
#             if confidence >= confidence_threshold and cls == 0:  # YOLO מזהה "person" כ- class 0
#                 people_count += 1
#                 # צביעה של הבוקס על התמונה
#                 x1, y1, x2, y2 = box.xyxy[0].tolist()
#                 cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
#
#     print(f"מספר האנשים שזוהו בתמונה: {people_count}")
#
#     # הצגת התמונה עם הבוקסות שסומנו
#     plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#     plt.axis('off')  # להסתיר את הצירים בתמונה
#     plt.show()
#
#     return people_count

# # קריאה לפונקציה עם התמונה הרצויה
# image_path = r"C:\Users\1\Downloads\אנשים בתור בלילה.jpeg"
# detect_people_in_image(image_path)
# import os
# graph = Graph()
#
# file_path = "C:/Users/1/Desktop/full_project/Data/park_data.xml"
# print(f"בודק אם הקובץ קיים בנתיב: {file_path}")
#
# if not os.path.exists(file_path):
#     print(f"הקובץ {file_path} לא נמצא!")
# else:
#     load_from_xml(graph, file_path)
#
import torch
import cv2
import numpy as np

# from models.yolo import Model

# הגדרת הנתיב לקובץ המשקלות
weights_path = r"C:\Users\1\Desktop\full_project\Model\best.pt"

# טעינת המודל עם המשקלות
model = torch.load(weights_path)
model.eval() # הגדרת המודל למצב הערכה (evaluation)

# קריאת התמונה
image_path = &#39;path/to/your/image.jpg&#39;
image = cv2.imread(image_path)

# עיבוד התמונה (שינוי גודל, נרמול וכו&#39;)
image_resized = cv2.resize(image, (640, 640)) # שינוי גודל לדוגמה
image_normalized = image_resized / 255.0 # נרמול לדוגמה
image_tensor = torch.from_numpy(image_normalized).float().unsqueeze(0) # המרת
התמונה ל-tensor

# ביצוע חיזוי
with torch.no_grad():

predictions = model(image_tensor)