class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

#3----5---8-5-10-2-1
def create_link_list(inp,ref=4):
    ref_pt,pt,head=None,None,None
    for i,data in enumerate(inp):
        if head==None:
            head=Node(data)
            pt=head
        else:
            pt.next=Node(data)
            pt=pt.next
        if i==ref:
            ref_pt=pt
    return head,ref_pt

def partition_link_list(head,ref):
    if head==None or ref==None:
        return None
    head2,ptr,prev=None,head,None
    print( head2,ptr,prev,head,ref)
    while ptr:
        if ptr==head and ptr.val<ref.val:
            head=ptr.next
            ptr.next=head2
            head2=ptr
            ptr=head
        elif ptr.val<ref.val:
            prev.next=ptr.next
            ptr.next=head2
            head2=ptr
            ptr=prev.next
        else: 
            prev=ptr
            ptr=ptr.next
    ptr=head2
    while ptr:
        prev=ptr
        ptr=ptr.next
    prev.next=head
    head=head2
    return head

def print_ll(head):
    ptr=head
    while ptr:
        print(ptr.val,"-",end="")
        ptr=ptr.next
    print()


head,ref=create_link_list([3,5,8,5,10,2,1],3)
head=partition_link_list(head,ref)
print_ll(head)

head,ref=create_link_list([8,5,7,6,3,2,5,1,7,4],3)
head=partition_link_list(head,ref)
print_ll(head)