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

    def __fromStart(self,node,n):
        if n==1:
            print(node.data)
        elif node.next:
            self.__fromStart(node.next,n-1)
        else:
            print("N elements not there")
    
    def fromStart(self,n):
        self.__fromStart(self.head,n)

    def fromEnd(self,n):
        ptr=self.head
        while n:
            if not ptr:
                print("less than n elements")
                return
            ptr=ptr.next
            n=n-1
            
        ptr1=self.head
        while ptr:
            ptr=ptr.next
            ptr1=ptr1.next
        
        print(ptr1.data)


    
        
        


ll = LinkList()
ll.insertBeg("Mon")
ll.insertBeg("Tue")
ll.insertBeg("Thu")

ll.traverseList()
ll.fromStart(3)
ll.fromEnd(3)