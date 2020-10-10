# difference between dfs and topological sort is we first visit all the adjacent edges than we put
#the vertex in stack
class Graph:

    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[ [] for i in range(vertices) ]

    def add_edge(self,src,dest):
        self.edges[src].append(dest)

    def topological_sort(self):
        visited=[False for i in range(self.vertices)]
        stack = []
        for v in range(self.vertices):
            if not visited[v]:
                self._topological_sort_helper(v,visited,stack)
        
        print(stack[::-1])

    def _topological_sort_helper(self,vertex,visited,stack):
        print(vertex)
        visited[vertex]=True
        for v in self.edges[vertex]:
            if not visited[v]:
                self._topological_sort_helper(v,visited,stack)

        stack.append(vertex)


        


g= Graph(6) 
g.add_edge(5, 2) 
g.add_edge(5, 0) 
g.add_edge(4, 0) 
g.add_edge(4, 1) 
g.add_edge(2, 3) 
g.add_edge(3, 1)

g.topological_sort()