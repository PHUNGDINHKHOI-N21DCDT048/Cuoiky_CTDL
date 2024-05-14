from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor == v:
                    count += 1
        return count

 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 0)

vertex_to_check = 2

print(f"Số cung đi vào đỉnh {vertex_to_check} là: {g.SoCungVao(vertex_to_check)}")
