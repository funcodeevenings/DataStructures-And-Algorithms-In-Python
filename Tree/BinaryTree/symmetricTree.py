class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def is_symmetric(root):
    return is_mirror(root,root)

def is_mirror(root1,root2):
    if root1==None and root2==None:
        return True
    if root1 and root2 and root1.data == root2.data:
        return is_mirror(root1.left,root2.right) and is_mirror(root1.right,root2.left)
    return False
    


root = Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(4)
root.right.left=Node(4)
root.right.right=Node(3)

