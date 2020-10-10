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

def partition(head):
    pt,fp=head,head
    while fp.next and fp.next.next:
        pt=pt.next
        fp=fp.next.next

    fp=pt.next
    pt.next=None

    return head,fp

def merge(head1,head2):
    if not head1:
        return head2
    if not head2:
        return head1
    pt1,pt2=head1,head2
    if pt1.data<pt2.data:
        head=pt1
        pt1=pt1.next
    else:
        head=pt2
        pt2=pt2.next
    pt=head
    while pt1 and pt2:
        if pt1.data<pt2.data:
            pt.next=pt1
            pt1=pt1.next
        else:
            pt.next=pt2
            pt2=pt2.next
        pt=pt.next
    if pt1:
        pt.next=pt1
    if pt2:
        pt.next=pt2
    return head

def mergeSort(head):
    if not head or not head.next:
        return head
    a,b=partition(head)
    displayll(a)
    displayll(b)
    x=mergeSort(a)
    print("x=",end="")
    displayll(x)
    y=mergeSort(b)
    print("y=",end="")
    displayll(y)
    head=merge(x,y)
    print("head=",end="")
    displayll(head)
    return head


def displayll(head):
    ptr=head
    while ptr:
        print(ptr.data,"->",end="")
        ptr=ptr.next
    print("None")

h1=createLinkList([2,4,8,6,5,4,15,12])
displayll(h1)
mergeSort(h1)
displayll(h1)