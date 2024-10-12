import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

intersections = [
    "A", "B", "C", "D", "E", "F", "G", "H"
]
G.add_nodes_from(intersections)

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "E"),
    ("D", "E"),
    ("D", "F"),
    ("E", "F"),
    ("E", "G"),
    ("F", "H"),
    ("G", "H")
]
G.add_edges_from(edges)

plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа міста")
plt.show()

def dfs(graph, start, goal, path=[]):
    path = path + [start]
    if start == goal:
        return path
    if start not in graph:
        return None
    for node in graph[start]: 
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath
    return None

def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (node, path) = queue.pop(0)
        for adjacent in graph[node]:
            if adjacent not in path:
                if adjacent == goal:
                    return path + [adjacent]
                else:
                    queue.append((adjacent, path + [adjacent]))
    return None

start_node = "A"
goal_node = "H"

dfs_path = dfs(G, start_node, goal_node)
bfs_path = bfs(G, start_node, goal_node)

print(f"Шлях за допомогою DFS: {dfs_path}")
print(f"Шлях за допомогою BFS: {bfs_path}")