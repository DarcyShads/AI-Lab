class Graph:
    def __init__(self, graph, maxLim):
        self.graph = graph
        self.maxLim = maxLim

    def depth_limited_search(self, src, visited=set(), level=0):
        if level == maxLim:
            return

        visited.add(src)
        path = [src]

        for v in self.graph[src]:
            if v not in visited:
                path_ext = self.depth_limited_search(v, visited, level+1)
                path.extend(path_ext)

        return path


maxLim = 4
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

g = Graph(graph, maxLim)
path = g.depth_limited_search('0')
print('Path Traversed :', end=" ")
print(" -> ".join(path))
