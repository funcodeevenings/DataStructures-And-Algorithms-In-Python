import collections
class Queue:
    def __init__(self):
        self.q=collections.deque([])

    def push(self,item):
        self.q.append(item)

    def pop(self):
        return self.q.popleft() #O(k) hence its better to use dequeue

    def peek(self):
        return self.q[0]

    def isEmpty(self):
        if not self.q:
            return True
        else:
            return False

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def level_order_insert(self, data):
        q = Queue()
        q.push(self)
        while not q.isEmpty():
            n = q.pop()
            if not n.left:
                n.left = Node(data)
                return
            else:
                q.push(n.left)
            if not n.right:
                n.right = Node(data)
                return
            else:
                q.push(n.right)

    def preorder(self):
        print(self.data)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(12)
root.level_order_insert(6)
root.level_order_insert(14)
root.level_order_insert(3)
root.preorder()
root.PrintTree()