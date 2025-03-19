from packages import*
from my_graph import Graph  # נניח שזו המחלקה שמנהלת את הגרף
from XML_Loader import XML_Loader  # ייבוא מחלקת טעינת ה-XML

graph = Graph()
# טעינת הנתונים מקובץ XML
xml_loader = XML_Loader(graph)  # יצירת אובייקט מסוג XML_Loader
xml_loader.load_from_xml("park_data.xml")  # טעינת הנתונים לגרף

ver= graph.get_vertices()
print(ver)
edg= edges = graph.get_all_edges(20)
print(edg)

