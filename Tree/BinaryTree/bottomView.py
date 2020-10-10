class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def bottom_view(root):
    if not root:
        return
        
    q=[(root,0)]
