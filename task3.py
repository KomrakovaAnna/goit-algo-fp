import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
    
    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        min_heap = [(0, src)]
        
        while min_heap:
            distance, u = heapq.heappop(min_heap)
            
            if distance > dist[u]:
                continue
            
            for neighbor, weight in self.graph[u]:
                if dist[u] + weight < dist[neighbor]:
                    dist[neighbor] = dist[u] + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        
        return dist

g = Graph(9)
g.add_edge(0, 1, 4)
g.add_edge(0, 7, 8)
g.add_edge(1, 2, 8)
g.add_edge(1, 7, 11)
g.add_edge(2, 3, 7)
g.add_edge(2, 8, 2)
g.add_edge(2, 5, 4)
g.add_edge(3, 4, 9)
g.add_edge(3, 5, 14)
g.add_edge(4, 5, 10)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(6, 8, 6)
g.add_edge(7, 8, 7)

distances = g.dijkstra(0)

print("Відстань від вершини 0 до інших вершин графа:")
for i, d in enumerate(distances):
    print(f"До вершини {i} найкоротша відстань: {d}")

