# DICT_GRAPH = { }

# class Node:
#     def __init__(self, data):
#         self.data = data
# class Structure:
#     def create_node(self, data):
#         node = Node(data)
#     def create_relation(self, A, B ):
#         DICT_GRAPH[A] = [B]
        
        
        
        
        
# DICT_GRAPH = {}

# class Node:
#     def __init__(self, data):
#         self.data = data


# class Structure:
#     def create_node(self, data):
#         node = Node(data)

#         if node.data not in DICT_GRAPH:
#             DICT_GRAPH[node.data] = []
#         return node
#     def create_relation(self, A, B):
#         if A not in DICT_GRAPH:
#             DICT_GRAPH[A] = []

#         if B not in DICT_GRAPH:
#             DICT_GRAPH[B] = []

#         DICT_GRAPH[A].append(B)
#         DICT_GRAPH[B].append(A)

#     def display(self):
#         for vertex, neighbors in DICT_GRAPH.items():
#             print(vertex, "-", neighbors)

# graph = Structure()

# graph.create_node("A")
# graph.create_node("B")
# graph.create_node("C")
# graph.create_node("D")

# graph.create_relation("A", "B")
# graph.create_relation("A", "C")
# graph.create_relation("B", "D")
# graph.create_relation("C", "D")

# graph.display()


# DICT_GRAPH = {}

# class Node:
#     def __init__(self, data):
#         self.data = data


# class Structure:
#     def create_node(self, data):
#         node = Node(data)
#         DICT_GRAPH[node.data] = []

#     def create_relation(self, A, B):
#         DICT_GRAPH[A].append(B)
#         DICT_GRAPH[B].append(A)

#     def display(self):
#         for node in DICT_GRAPH:
#             print(node, ":", DICT_GRAPH[node])


# graph = Structure()

# # Create Nodes
# graph.create_node("A")
# graph.create_node("B")
# graph.create_node("C")
# graph.create_node("D")

# # Create Relations
# graph.create_relation("A", "B")
# graph.create_relation("A", "C")
# graph.create_relation("B", "D")
# graph.create_relation("C", "D")

# # Display Graph
# graph.display()

DICT_GRAPH = {}

class Node:
    def __init__(self, data):
        self.data = data

class Structure:
    def create_node(self, data):
        node = Node(data)
        DICT_GRAPH[node] = []
        return node

    def create_relation(self, A, B):
        DICT_GRAPH[A].append(B)
        DICT_GRAPH[B].append(A)

    def display(self):
        for node in DICT_GRAPH:
            print(hex(id(node)), ":", [hex(id(n)) for n in DICT_GRAPH[node]])


graph = Structure()

A = graph.create_node("A")
B = graph.create_node("B")
C = graph.create_node("C")
D = graph.create_node("D")

graph.create_relation(A, B)
graph.create_relation(A, C)
graph.create_relation(B, D)
graph.create_relation(C, D)

graph.display()



