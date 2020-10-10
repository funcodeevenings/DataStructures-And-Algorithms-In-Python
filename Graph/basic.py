class Graph: 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[] for x in range (vertices)]
        self.visited= [False for x in range(vertices)]
  
    # Function to add an edge in an undirected graph 
    def add_edge(self, src, dest): 
        # Adding the node to the source node 
        self.graph[src].append(dest)
        
    def is_connected(self,src):
        q = [src]
        while q:
            ver=q.pop(0)
            if not self.visited[ver]:
                q.extend(self.graph[ver])
                self.visited[ver] = True
        for x in range(self.V):
            if not self.visited[x]:
                return False
        return True
        
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        v = len(rooms)
        g = Graph(v)
        for i,lis in enumerate(rooms):
            for j in lis:
                print(i,j)
                g.add_edge(i,j)
        return g.is_connected(0)
                