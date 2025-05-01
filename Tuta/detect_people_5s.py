# def detect_people_5s(video_paths):
#     """
#     הפונקציה מקבלת רשימה של נתיבי סרטונים, מזהה אנשים ומחזירה את ממוצע מספר האנשים
#     לאחר 5 שניות בסרטונים השונים. אם לא זוהו אנשים, מחזירה 0.
#     """
#     if not isinstance(video_paths, list) or not video_paths:
#         raise ValueError(f"נתיב הווידאו לא תקין: {video_paths}")
#
#     total_people = 0  # משתנה לשמירת סך האנשים שנמצאו בכל הסרטונים
#     total_frames = 0  # משתנה לשמירת מספר הפריימים הכולל (למדוד ממוצע)
#
#     for video_path in video_paths:  # עבור כל נתיב בסרטון
#         cap = cv2.VideoCapture(video_path)  # פתיחת סרטון באמצעות OpenCV
#         if not cap.isOpened():
#             raise ValueError(f"לא ניתן לפתוח את הסרטון: {video_path}")
#
#         start_time = None  # משתנה לשמירת הזמן שבו זוהה אדם לראשונה
#         detected_people = 0  # משתנה לשמירת מספר האנשים שזוהו
#         frame_count = 0  # משתנה הסופר את מספר הפריימים בסרטון
#
#         detected_people_avg = 0  # אתחול ברירת מחדל של ממוצע האנשים
#
#         while cap.isOpened():  # לולאה שפועלת כל עוד הסרטון פתוח
#             frame_count += 1
#             ret, frame = cap.read()  # קריאת הפריים הבא בסרטון
#             if not ret:  # אם הפריים לא תקין - צא מהלולאה
#                 break
#
#             results = model(frame)  # הרצת YOLO על הפריים הנוכחי
#             people_count = 0  # ספירת האנשים בפריים
#             for result in results:  # ריצה על אובייקטים שנמצאו בפריים הנוכחי
#                 for box in result.boxes:  # ריצה על התיבות שנמצאו באובייקט
#                     cls = int(box.cls[0])  # מזהה את הקלאס של האובייקט
#                     if cls == 0:  # YOLO מזהה "person" כ- class 0
#                         people_count += 1  # ספירת האנשים שזוהו
#
#             detected_people += people_count  # סיכום אנשים שזוהו עד כה
#             if people_count > 0:  # אם זוהה לפחות אדם אחד
#                 if start_time is None:  # אם זו הפעם הראשונה שזוהה אדם, נתחיל למדוד זמן
#                     start_time = time.time()  # שמירת הזמן הנוכחי
#
#                 elapsed_time = time.time() - start_time  # מחשב כמה זמן עבר מאז הזיהוי הראשון
#
#                 if elapsed_time >= 5:  # אם עברו 5 שניות מאז הזיהוי הראשון
#                     detected_people_avg = detected_people / frame_count  # חישוב ממוצע האנשים שנמצאו
#                     print(f"Captured frame after 5 seconds with average people count: {detected_people_avg}")
#                     break  # עצירת הלולאה לאחר סיום הספירה
#
#         cap.release()  # סגירת החלונות שנפתחו עם האובייקט שיצרנו cv2.VideoCapture()
#
#         # אם לא זוהו אנשים בסרטון, נדפיס הודעה ונהפוך את ממוצע האנשים ל-0
#         if detected_people == 0:
#             print(f"לא זוהו אנשים בסרטון {video_path}. זמן המתנה יהיה 0.")
#             detected_people_avg = 0  # ערך ברירת מחדל במקרה שלא זוהו אנשים
#
#         total_people += detected_people_avg  # הוספת ממוצע האנשים מהסרטון הזה לסך הכולל
#         total_frames += 1  # ספירת הסרטונים
#
#     if total_frames > 0:
#         return total_people / total_frames  # חישוב ממוצע האנשים בכל הסרטונים
#     else:
#         return 0  # אם לא היו סרטונים, החזר 0
