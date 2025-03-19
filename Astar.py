from my_graph import Graph
from packages import *
class AStarAlgorithm:
    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, current, goal):
        pos1 = self.graph.get_vertex_data(current).get("pos")
        pos2 = self.graph.get_vertex_data(goal).get("pos")

        if pos1 is None or pos2 is None:
            return float('inf')

        return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)
