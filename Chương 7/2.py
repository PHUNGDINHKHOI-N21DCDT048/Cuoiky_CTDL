from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFSUtil(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def SoThanhPhan(self):
        V = len(self.graph)
        visited = [False] * V
        count = 0
        for v in range(V):
            if visited[v] == False:
                self.DFSUtil(v, visited)
                count += 1
        return count


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(3, 4)
print("Số thành phần liên thông của đồ thị là:", g.SoThanhPhan())
