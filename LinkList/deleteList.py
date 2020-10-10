class Node:
    def __init__(self,data):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head=None
    
    def insertBeg(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def traverse(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
        
    def deleteList(self):
        ptr = self.head
        while ptr:
            next = ptr.next
            ptr.next=None
            del ptr
            ptr=next
        self.head=None



ll = LinkList()
ll.insertBeg("Mon")
ll.insertBeg("Tue")
ll.insertBeg("Thu")

ll.traverse()

ll.deleteList()

ll.traverse()