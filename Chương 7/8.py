from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DuongDi(self, v1, v2):
        visited = set()

        def DFSUtil(v):
            if v == v2:
                return True
            visited.add(v)
            for neighbour in self.graph[v]:
                if neighbour not in visited:
                    if DFSUtil(neighbour):
                        return True
            return False

        return DFSUtil(v1)

 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)

vertex1 = 0
vertex2 = 3

if g.DuongDi(vertex1, vertex2):
    print(f"Có đường đi từ đỉnh {vertex1} đến đỉnh {vertex2}")
else:
    print(f"Không có đường đi từ đỉnh {vertex1} đến đỉnh {vertex2}")
