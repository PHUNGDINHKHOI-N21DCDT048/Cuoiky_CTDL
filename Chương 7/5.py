from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BacDinh(self, v):
        return len(self.graph[v])

 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)

vertex_to_check = 2

print(f"Bậc của đỉnh {vertex_to_check} là: {g.BacDinh(vertex_to_check)}")
