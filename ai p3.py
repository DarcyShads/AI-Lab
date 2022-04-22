from queue import PriorityQueue as PQ


class Graph:
    def __init__(self, vertices, beamWidth):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]
        self.beamWidth = beamWidth

    def add_edge(self, node1, node2, cost):
        self.graph[node1].append((node2, cost))
        self.graph[node2].append((node1, cost))

    def beam_search_algorithm(self, src, goal):
        visited = [0]*self.vertices
        pq = PQ()
        pq.put((0, src))
        visited[src] = 1
        path = []
        while not pq.empty():
            u = pq.get()[1]
            path.append(u)
            if u == goal:
                print("Path Found :", end=" ")
                print(" -> ".join(map(str, path)))
                return path

            for v, c in self.graph[u]:
                if not visited[v]:
                    pq.put((c, v))
                    visited[v] = 1

            temp_pq = PQ()
            i = 1
            while not pq.empty() and self.beamWidth >= i:
                temp_pq.put(pq.get())
                i += 1
            pq = temp_pq

        print("Path Not Found")
        return None


if __name__ == "__main__":
    graph = Graph(vertices=5, beamWidth=2)

    graph.add_edge(0, 2, 8)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 12)
    graph.add_edge(2, 3, 6)
    graph.add_edge(1, 4, 13)
    graph.add_edge(4, 3, 3)

    source = 0
    destination = 2

    graph.beam_search_algorithm(source, destination)
