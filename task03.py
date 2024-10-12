import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

intersections = [
    "A", "B", "C", "D", "E", "F", "G", "H"
]
G.add_nodes_from(intersections)

edges_with_weights = [
    ("A", "B", 1),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 2),
    ("C", "E", 5),
    ("D", "E", 2),
    ("D", "F", 4),
    ("E", "F", 1),
    ("E", "G", 3),
    ("F", "H", 1),
    ("G", "H", 2)
]
G.add_weighted_edges_from(edges_with_weights)

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
plt.title("Транспортна мережа міста з вагами")
plt.show()

def dijkstra_all_pairs(graph):
    shortest_paths = {}
    for node in graph.nodes:
        lengths, paths = nx.single_source_dijkstra(graph, node)
        shortest_paths[node] = (lengths, paths)
    return shortest_paths

shortest_paths = dijkstra_all_pairs(G)

for start_node, (lengths, paths) in shortest_paths.items():
    print(f"Вершина {start_node}:")
    for target_node in paths.keys():
        print(f"  Найкоротший шлях до {target_node} = {paths[target_node]} з вагою {lengths[target_node]}")