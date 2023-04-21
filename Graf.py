import networkx as nx
import matplotlib.pyplot as plt
import random

# Tworzenie pustego grafu
G = nx.Graph()

# Dodawanie wierzchołków
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Dodawanie losowych krawędzi
for i in range(20): # Dodanie 20 losowych krawędzi
    u = random.randint(1, 10) # Wylosowanie pierwszego wierzchołka
    v = random.randint(1, 10) # Wylosowanie drugiego wierzchołka
    w = random.randint(1, 20) # Wylosowanie wagi krawędzi
    G.add_edge(u, v, weight=w)

# Określenie pozycji wierzchołków w grafie
pos = nx.spring_layout(G)

# Rysowanie grafu
nx.draw(G, pos=pos, with_labels=True)

# Dodawanie etykiet krawędzi
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()


# Wyznaczanie najkrótszych ścieżek z wierzchołka 1
source = 1
shortest_paths = nx.shortest_path(G, source=source)

# Wypisanie najkrótszych ścieżek
for target in shortest_paths:
    path = shortest_paths[target]
    print(f"Najkrótsza ścieżka z {source} do {target}: {path}, o długości {len(path)-1}")
