import math  # ייבוא מודול למתודולוגיית חישוב המרחקים
from ultralytics import YOLO
import cv2
import xml.etree.ElementTree as ET  # ייבוא מודול לעבודה עם קבצי XML
import matplotlib.pyplot as plt  # ייבוא מודול לציור גרפים
import networkx as nx  # ייבוא מודול ליצירת גרפים

# טוען את המודל של YOLOv11
model = YOLO(r"C:\Users\1\Desktop\full_Project\Model\yolo11n.pt")  # ניתן לשנות לגרסה אחרת אם צריך

# השתקת הדפסות פנימיות של YOLO
model.overrides['verbose'] = False
