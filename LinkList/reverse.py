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

    def reverse(self):
        p1=self.head
        if p1:
            p2=p1.next
        else:
            return
        while p1 is not None and p2 is not None:
            p3=p2.next
            print("1",p1.data,p2.data,self.head.data)
            p2.next=p1
            print("2",p1.data,p2.data,self.head.data)
            p1=p2
            print("3",p1.data,p2.data,self.head.data)
            p2=p3
            print("4",p1.data,self.head.data)
        self.head.next=None    
        self.head=p1
        print("5",self.head.data)



ll = LinkList()
ll.head = Node("Mon")
ll.insertBeg("Tue")
ll.insertBeg("Thu")
ll.traverseList()
ll.reverse()
ll.traverseList()