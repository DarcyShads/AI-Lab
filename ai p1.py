class Graph:
    def __init__(self, adjacency_list, h):
        self.adjacency_list = adjacency_list
        self.h = h

    def find_neighbours(self, n):
        return self.adjacency_list[n]

    def a_star_algorithm(self, source, goal):
        open_list = set([source])
        closed_list = set([])
        g = {source: 0}
        parent = {source: source}
        while len(open_list):
            n = None
            for v in open_list:
                if n == None or g[v]+self.h[v] < g[n]+self.h[n]:
                    n = v

            if n == None:
                print("No Path Found")
                return None

            if n == goal:
                path_followed = []
                while parent[n] != n:
                    path_followed.append(n)
                    n = parent[n]
                path_followed.append(n)
                path_followed.reverse()
                print("Path Followed : {}".format(path_followed))
                return path_followed

            for (m, weight) in self.find_neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    g[m] = g[n]+weight
                    parent[m] = n
                else:
                    if g[m] > g[n]+weight:
                        g[m] = g[n]+weight
                        parent[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist")
        return None


if __name__ == "__main__":

    adjacency_list = {
        'A': [('B', 1), ('C', 3), ('D', 7)],
        'B': [('D', 5)],
        'C': [('D', 12)]
    }

    h = {
        'A': 1,
        'B': 1,
        'C': 1,
        'D': 1
    }

    graph = Graph(adjacency_list, h)

    start_node = 'A'
    end_node = 'D'

    graph.a_star_algorithm(start_node, end_node)
