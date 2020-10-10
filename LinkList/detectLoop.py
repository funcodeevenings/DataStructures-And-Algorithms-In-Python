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
            print(ptr.data,end=",")
            ptr = ptr.next

    def detectLoop(self): 
        slow_p = self.head 
        fast_p = self.head 
        while(slow_p and fast_p and fast_p.next): 
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p: 
                print("Found Loop")
                return 
        print("No Loop Found!!")

ll = LinkList()
ll.insertBeg("Mon")
ll.insertBeg("Tue")
ll.insertBeg("Thu")
ll.traverseList()
ll.head.next.next=ll.head
ll.detectLoop()