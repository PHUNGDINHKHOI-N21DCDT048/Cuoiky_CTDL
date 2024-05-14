from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def SoCungRa(self, v):
        return len(self.graph[v])

 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)

vertex_to_check = 2

print(f"Số cung đi ra khỏi đỉnh {vertex_to_check} là: {g.SoCungRa(vertex_to_check)}")
