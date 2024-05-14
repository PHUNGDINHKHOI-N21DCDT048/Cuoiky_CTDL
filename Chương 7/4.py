from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def ChuaDinh(self, v):
        return v in self.graph


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)

vertex_to_check = 2

if g.ChuaDinh(vertex_to_check):
    print(f"Đỉnh {vertex_to_check} tồn tại trong đồ thị")
else:
    print(f"Đỉnh {vertex_to_check} không tồn tại trong đồ thị")
