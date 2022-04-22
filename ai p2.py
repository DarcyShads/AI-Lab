from queue import PriorityQueue as PQ


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, node1, node2, cost):
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))

    def best_first_search(self, src, goal):
        visited = [False]*self.vertices
        pq = PQ()
        pq.put((0, src))
        visited[src] = True
        path = []
        while not pq.empty():
            u = pq.get()[1]
            path.append(u)

            if u == goal:
                print("path found :", " -> ".join(map(str, path)))
                return path

            for v, c in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    pq.put((c, v))

        print("Path Not Found")
        return None


if __name__ == '__main__':

    g = Graph(5)

    g.add_edge(0, 2, 8)
    g.add_edge(1, 2, 12)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 4, 13)
    g.add_edge(2, 3, 6)
    g.add_edge(4, 3, 3)

    source = 0
    destination = 2

    g.best_first_search(source, destination)
