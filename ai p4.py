class Graph:
    def __init__(self, graph):
        self.graph = graph

    def depth_first_search(self, src, visited=set()):
        visited.add(src)
        path = [src]

        for v in self.graph[src]:
            if v not in visited:
                path.extend(self.depth_first_search(v, visited))
        return path


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}


g = Graph(graph)
path = g.depth_first_search('0')
print(" -> ".join(path))
