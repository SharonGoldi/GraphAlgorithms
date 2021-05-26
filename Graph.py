from collections import defaultdict


# a general class for a graph
class Graph:

    def __init__(self, num_of_vertex):
        self.V = num_of_vertex
        self.graph = defaultdict(list)

    # add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # transpose the edge matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # the recursive dfs inner func
    def __dfs(self, d, visited, vertex_ordered, print_forest):
        visited[d] = True
        vertex_ordered.append(d)
        for u in self.graph[d]:
            if not visited[u]:
                if print_forest:
                    print(d, '->', u, '/')
                self.__dfs(u, visited)

    # returns the vertex in the dfs order, if wanted prints the dfs forest
    def dfs(self, d, print_forest):
        visited = [False] * self.V
        vertex_ordered = []
        self.__dfs(d, visited, vertex_ordered, print_forest)
        return vertex_ordered

    # returns the vertex in the bfs order, if wanted prints the bfs tree
    def bfs(self, d, print_tree):
        visited = [False] * self.V
        queue = []
        vertex_ordered = []

        visited[d] = True
        queue.append(d)
        vertex_ordered.append(d)
        while queue:
            u = queue.pop()
            vertex_ordered.append(u)
            for v in self.graph[u]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    if print_tree:
                        print(u, '->', v, '/')
        return vertex_ordered

    # print the SCC - O(V+E)
    def scc(self):
        stack = []
        visited = [False] * self.V
        g_transpose = self.transpose()

        for u in range(self.V):
            if not visited[u]:
