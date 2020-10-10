class DisjointSet:
    def __init__(self,size):
        self.parent=[-1]*size
    
    # A utility function to find the subset of an element i 
    def find_parent(self,i): 
        if self.parent[i] == -1: 
            return i 
        if self.parent[i]!= -1: 
             return self.find_parent(parent[i]) 
  
    # A utility function to do union of two subsets 
    def union(self,x,y): 
        x_set = self.find_parent(x) 
        y_set = self.find_parent(y) 
        parent[x_set] = y_set 
  