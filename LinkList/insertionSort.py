class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

    
def createLinkList(nums):
    if not nums:
        return None
    head = Node(nums[0])
    ptr=head
    for num in nums[1:]:
        ptr.next=Node(num)
        ptr=ptr.next
    return head

def insertionSort(head):
    if not head:
        return None
    head2=head
    head=head.next
    head2.next=None
    ptr=head
    while ptr:
        node=ptr
        ptr=ptr.next
        node.next=None
        head2=insertSorted(head2,node)
    return head2

def insertSorted(head,node):
    if not node:
        return head
    prev,ptr=None,head
    while ptr:
        if ptr.data<node.data:
            prev=ptr
            ptr=ptr.next
        else:
            break
    if not ptr:
        prev.next=node
    elif not prev:
        node.next=head
        head=node
    else:
        prev.next=node
        node.next=ptr
    return head

def displayll(head):
    ptr=head
    while ptr:
        print(ptr.data,"->",end="")
        ptr=ptr.next
    print("None")

h1=createLinkList([2,4,8,6,5,4,15,12])
displayll(h1)
insertionSort(h1)
displayll(h1)