'''1. Create an undirected graph with the following connections:

   * A - B
   * A - C
   * B - D
   * C - D

   Display all the vertices and their connected neighbors.
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

#     def display(self):
#         for vertex, neighbors in self.graph.items():
#             print(f"{vertex}: {', '.join(neighbors)}")


# graph = Graph()

# graph.add_edge('A', 'B')
# graph.add_edge('A', 'C')
# graph.add_edge('B', 'D')
# graph.add_edge('C', 'D')

# graph.display()

# class Graph:
#     def __init__(self):
#         self.graph = {}
#     def add edge(self, vertex1, vertex2):
#         if vertex1 not in self.graph:
#             self.graph[vertex1] = []
#             if vertex2 not in self.gragh:
#                 self.graph[vertex2] = []
                
#             else:
#                 self.graph[vertex1].append(vertex2)
#                 self.graph[vertex2].append(vertex1)
#     def display(self):
#         for vertex, neighbors in self.graph.items():
#             print(f"{vertex}: {','.join(neighbors)}")

# graph = Graph()

# graph.add_edge('A', 'B')
# graph.add_edge('C', 'D')
# graph.add_edge('E', 'F')
# graph.add_edge('G', 'H')
# graph.display()


                