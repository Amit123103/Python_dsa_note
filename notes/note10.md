Here's a very simple **Graph example** for a beginner.

### Graph Structure

```text
A ----- B
|       |
|       |
C ----- D
```

---

### Python Code

```python
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, v1, v2):
        if v1 not in self.graph:
            self.graph[v1] = []

        if v2 not in self.graph:
            self.graph[v2] = []

        self.graph[v1].append(v2)
        self.graph[v2].append(v1)   # Undirected graph

    def display(self):
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])


# Create Graph
g = Graph()

# Add edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')

# Display graph
g.display()
```

### Output

```text
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A', 'D']
D -> ['B', 'C']
```

---

### How it Works

When you write:

```python
g.add_edge('A', 'B')
```

the graph becomes:

```text
A ----- B
```

Dictionary:

```python
{
    'A': ['B'],
    'B': ['A']
}
```

---

When you add:

```python
g.add_edge('A', 'C')
```

Graph:

```text
    A
   / \
  B   C
```

Dictionary:

```python
{
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A']
}
```

---

When you add:

```python
g.add_edge('B', 'D')
g.add_edge('C', 'D')
```

Graph:

```text
    A
   / \
  B   C
   \ /
    D
```

---

### Real-Life Example

Think of:

* Vertices = People
* Edges = Friendships

```text
Amit ---- Rahul
  |
Neha
```

Here:

* Amit is friends with Rahul.
* Amit is friends with Neha.

This is exactly how social media connections are stored using graphs.

### Exam Definition

**Graph:** A graph is a non-linear data structure consisting of vertices (nodes) and edges (connections) used to represent relationships between objects.
