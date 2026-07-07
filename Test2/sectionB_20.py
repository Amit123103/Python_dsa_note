'''20.Perform a Depth-First Search (DFS) traversal starting from vertex A.'''

class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, node, visited):
        visited.append(node)
        print(node, end=" ")

        for i in self.graph[node]:
            if i not in visited:
                self.dfs(i, visited)

graph1 = Graph()

graph1.addEdge("A", "B")
graph1.addEdge("A", "C")
graph1.addEdge("B", "D")
graph1.addEdge("C", "D")

visited = []

print("DFS Traversal:")
graph1.dfs("A", visited)