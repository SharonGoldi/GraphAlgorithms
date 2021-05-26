from collections import defaultdict


# a general class for a directed graph
class Graph:

    def __init__(self, num_of_vertex):
        self.V = num_of_vertex
        self.graph = defaultdict(list)
        self.weights = defaultdict(list)
        self.positive_w = True

    # add edge into the graph
    def add_edge(self, s, d, w=1):
        self.graph[s].append(d)
        self.weights[s,d].append(w)

        if w < 0 and self.positive_w:
            self.positive_w = False

    # transpose the edge matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # the recursive dfs inner func
    def __dfs(self, d, visited, vertex_ordered_i, vertex_ordered_f, print_forest):
        visited[d] = True
        vertex_ordered_i.append(d)
        for u in self.graph[d]:
            if not visited[u]:
                if print_forest:
                    print(d, '->', u, ' ')
                self.__dfs(u, visited)
        vertex_ordered_f.append(d)

        return vertex_ordered_i, vertex_ordered_f

    # returns the vertex in the dfs order, if wanted prints the dfs forest
    def dfs(self, d=0, print_forest=True):
        visited = [False] * self.V
        vertex_ordered_i = []
        vertex_ordered_f = []
        self.__dfs(d, visited, vertex_ordered_i, vertex_ordered_f, print_forest)
        return vertex_ordered_i, vertex_ordered_f

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
                        print(u, '->', v, ' ')
        return vertex_ordered

    # returns the scc, if wanted, prints the SCC - O(V+E)
    def scc(self, print_scc=True):
        scc = []
        dfs_order_i, dfs_order_f = self.dfs(0)
        g_transpose = self.transpose(0)

        visited = [False] * self.V

        while dfs_order_f:
            u = dfs_order_f.pop()
            if not visited[u]:
                i, f = g_transpose.__dfs(u, visited, [], [], print_scc)
                if print_scc:
                    print("/")
                scc.append(f)
        return scc

    # returns the MST calced by Prim's algorithm, if wanted, prints it
    def MST_Prim(self):
        pass

    # returns the MST calced by Kruskal's algorithm, if wanted, prints it
    def MST_Kruskal(self):
        pass