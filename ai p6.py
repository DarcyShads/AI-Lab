class Graph:
    def __init__(self, vertices):
        self.graph = [[] for _ in range(vertices)]
        self.vertices = vertices

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def BFS(self, src):
        visited = [0]*self.vertices
        queue = [src]
        visited[src] = 1
        path = []
        while len(queue):
            u = queue[0]
            path.append(u)
            queue.pop(0)
            for v in self.graph[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = 1
        return path


if __name__ == "__main__":
    graph = Graph(5)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(0, 1)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(4, 3)
    path = graph.BFS(0)
    print("Path Traversed :", end=" ")
    print(" -> ".join(map(str, path)))
