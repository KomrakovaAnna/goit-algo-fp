import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import uuid

class Node:
    def __init__(self, key):
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла
        self.val = key  # Значення вузла
        self.left = None  # Лівий нащадок
        self.right = None  # Правий нащадок

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    # Функція для додавання вузлів і ребер до графа
    if node is not None:
        graph.add_node(node.id, label=node.val)
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def generate_colors(n, start_color, end_color):
    # Генерація градієнту кольорів від темного до світлого
    start_rgb = np.array(start_color) / 255.0
    end_rgb = np.array(end_color) / 255.0
    return [start_rgb + (end_rgb - start_rgb) * i / (n - 1) for i in range(n)]

def dfs_visit(graph, node_id, colors, order, color_map):
    # Відвідування вузлів у порядку обходу в глибину
    colors[node_id] = color_map[order]
    order += 1
    for neighbor_id in graph.neighbors(node_id):
        if neighbor_id not in colors:
            dfs_visit(graph, neighbor_id, colors, order, color_map)

def visualize_dfs(graph, pos, labels, start_color, end_color):
    # Візуалізація обходу в глибину з різнокольоровими вузлами
    colors = {}
    order = 0
    color_map = generate_colors(len(labels), start_color, end_color)
    for node_id in graph:
        if node_id not in colors:
            dfs_visit(graph, node_id, colors, order, color_map)
    node_colors = [colors[node] for node in graph]
    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, labels=labels, node_color=node_colors, node_size=1500, arrows=False)
    plt.title('Візуалізація DFS')
    plt.show()

def visualize_bfs(graph, pos, labels, start_color, end_color):
    # Візуалізація обходу в ширину з різнокольоровими вузлами
    colors = {}
    queue = deque()
    order = 0
    color_map = generate_colors(len(labels), start_color, end_color)
    queue.append(list(graph.nodes())[0])
    while queue:
        node_id = queue.popleft()
        if node_id not in colors:
            colors[node_id] = color_map[order]
            order += 1
            for neighbor_id in graph.neighbors(node_id):
                if neighbor_id not in colors:
                    queue.append(neighbor_id)
    node_colors = [colors[node] for node in graph]
    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos, labels=labels, node_color=node_colors, node_size=1500, arrows=False)
    plt.title('Візуалізація BFS')
    plt.show()

# Створення структури дерева
root = Node('Root')
root.left = Node('Left Child')
root.right = Node('Right Child')
root.left.left = Node('Left Grandchild')
root.right.right = Node('Right Grandchild')

# Створення графа зі структури дерева
G = nx.DiGraph()
pos = {}  
add_edges(G, root, pos) 

# Отримання міток для вузлів
labels = {n: G.nodes[n]['label'] for n in G.nodes}

# Візуалізація обходу дерева
visualize_dfs(G, pos, labels, (25, 25, 112), (135, 206, 250))  
visualize_bfs(G, pos, labels, (25, 25, 112), (135, 206, 250))  


