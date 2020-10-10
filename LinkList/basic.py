class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head=None

    def insertBeg(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head=newNode

    def traverseList(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next


ll = LinkList()
ll.head = Node("Mon")
ll.insertBeg("Tue")
ll.insertBeg("Thu")

ll.traverseList()