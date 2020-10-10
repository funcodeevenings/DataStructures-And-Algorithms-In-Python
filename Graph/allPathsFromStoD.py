class Graph:

    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[ [] for i in range(vertices) ]
        self.paths=[]

    def add_edge(self,src,dest):
        self.edges[src].append(dest)

    def find_all_paths(self,src,dest):
        self.paths=[]
        self._dfs(src,dest,[])
        print(self.paths)

    def _dfs(self,src,dest,path):
        path.append(src)
        if src==dest:
            self.paths.append(path.copy)
            path.pop()
            return
        for vertex in self.edges[src]:
            if not vertex in path:
                self._dfs(vertex,dest,path)
        return


g=Graph(4)
g.add_edge(0,2)
g.add_edge(2,0)
g.add_edge(2,1)
g.add_edge(0,3)
g.add_edge(1,3)
g.add_edge(0,1)

g.find_all_paths(2,3)