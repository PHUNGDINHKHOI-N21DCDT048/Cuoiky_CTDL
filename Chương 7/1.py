from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.DFS(i, visited)

    def is_connected(self):
        visited = [False] * (len(self.graph))
        self.DFS(next(iter(self.graph)), visited)
        for i in visited:
            if not i:
                return False
        return True

 
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

if g.is_connected():
    print("Đồ thị là đồ thị liên thông.")
else:
    print("Đồ thị không phải là đồ thị liên thông.")
