'''2. Given a graph, determine whether there is a direct connection (edge) between two given vertices.
'''

# class Graph:
#     def __init__(self):
#         self.graph = {}
#     def add_edge(self, vertex1, vertex2):
#         if vertex1 not in self.graph:
#             self.graph[vertex1] = []
#         if vertex2 not in self.graph:
#             self.graph[vertex2] = []
#         self.graph[vertex1].append(vertex2)
#         self.graph[vertex2].append(vertex1)
#     def h_edge(self, vertex1, vertex2):
#         if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
#             return True
#         return False
#     def display(self):
#         for vertex, neighbors in self.graph.items():
#             print(f"{vertex}: {','.join(neighbors)}")

# graph= Graph()

# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.display()