import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def visualize_heap(heap):

    G = nx.DiGraph()
    positions = {}
    n = len(heap)
    
    # Створюємо бінарне дерево
    for i in range(n):
        G.add_node(i, label=heap[i])
        # Якщо вузол не є коренем, додаємо до нього край
        if i != 0:
            G.add_edge((i - 1) // 2, i)
            
        level = int(np.log2(i + 1))
        offset = 2 ** (level + 1)
        x = i - 2 ** level + 1
        x = x * offset
        y = -level
        positions[i] = (x, y)
    
    labels = nx.get_node_attributes(G, 'label')
    colors = ['skyblue' for node in G.nodes()]
    
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos=positions, labels=labels, node_size=1500, node_color=colors, arrows=False)
    plt.title('Binary Heap Visualization')
    plt.show()

heap = [1, 3, 5, 7, 9, 2, 4]
visualize_heap(heap)

