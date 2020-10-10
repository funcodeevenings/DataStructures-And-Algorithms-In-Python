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

    def lengthIter(self):
        ptr=self.head
        count=0
        while ptr:
            ptr=ptr.next
            count=count+1
        return count
    
    def __lengthRec__(self,node):
        if node:
            return 1+ self.__lengthRec__(node.next)
        else:
            return 0

    def lengthRec(self):
        return self.__lengthRec__(self.head)


ll = LinkList()
ll.insertBeg("Mon")
ll.insertBeg("Tue")
ll.insertBeg("Thu")
print(ll.lengthIter())
ll.insertBeg("Thu")
print(ll.lengthRec())