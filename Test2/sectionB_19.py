'''19.Perform a Breadth-First Search (BFS) traversal starting from vertex A.'''

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
    def bfs(self, start):
        visited = []
        queue = []

        visited.append(start)
        queue.append(start)
        while len(queue) > 0:
            node = queue.pop(0)
            print(node, end=" ")

            for i in self.graph[node]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)

graph1 = Graph()
graph1.addEdge("A", "B")
graph1.addEdge("A", "C")
graph1.addEdge("B", "D")
graph1.addEdge("C", "D")

print("BFS Traversal:")
graph1.bfs("A")