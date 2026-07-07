'''18.Check whether there is a direct edge between two given vertices.'''

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
    def checkEdge(self, u, v):
        if v in self.graph[u]:
            print("Edge Exists")
        else:
            print("Edge Does Not Exist")

graph1 = Graph()

graph1.addEdge("A", "B")
graph1.addEdge("A", "C")
graph1.addEdge("B", "D")
graph1.addEdge("C", "D")

graph1.checkEdge("A", "B")
graph1.checkEdge("A", "D")


