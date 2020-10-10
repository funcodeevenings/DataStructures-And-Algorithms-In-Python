class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.totalSum = 0

    def insert(self, parentVal, node, direction):
        if self.data==parentVal:
            if direction=='L':
                self.left=node
            if direction=='R':
                self.right=node
            return
        if self.left:
            return self.left.insert(parentVal,node,direction)
        if self.right:
            return self.right.insert(parentVal,node,direction)


    def rootToLeafSum(self,root,pathSum):
        pathSum = pathSum*10+self.data
        if self.left:
            self.left.rootToLeafSum(root,pathSum)
        if self.right:
            self.right.rootToLeafSum(root,pathSum)
        if not(self.left or self.right):
            root.totalSum = root.totalSum+pathSum



        

t = int(input())
while t:
    t=t-1
    nodes=int(input())
    lis=input().strip().split()
    root = Node(int(lis[0]))
    for i in range(0,nodes*3,3):
        parentVal,nodeVal,direction=int(lis[i]),int(lis[i+1]),lis[i+2]
        node=Node(nodeVal)
        root.insert(parentVal,node,direction)
    
    totalSum=0
    root.rootToLeafSum(root,0)
    print(root.totalSum)

