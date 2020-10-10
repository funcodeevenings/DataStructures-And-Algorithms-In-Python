class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

def add_forward(head1,head2):
    len1=find_len(head1)
    len2=find_len(head2)
    if len1<len2:
        head1=pad(head1,len2-len1)
    else:
        head2=pad(head2,len1-len2)
    carry,head3=recursive_add(head1,head2)
    if carry:
        temp=head3
        head3=Node(carry)
        head3.next=temp
    return head3

def find_len(head):
    ptr,count=head,0
    while ptr:
        count=count+1
        ptr=ptr.next
    return count

def pad(head,len):
    if not head:
        return
    while len>0:
        temp=head
        head=Node(0)
        head.next=temp
        len=len-1
    return head

def recursive_add(head1,head2):
    if head1==None and head2==None:
        return 0,None
    carry,head3=recursive_add(head1.next,head2.next)
    sum=head1.val+head2.val+carry
    carry=sum//10
    if head3==None:
        head3=Node(sum%10)
    else :
        temp=head3
        head3=Node(sum%10)
        head3.next=temp

    return carry,head3

def create_link_list(inp):
    pt,head=None,None
    for i,data in enumerate(inp):
        if head==None:
            head=Node(data)
            pt=head
        else:
            pt.next=Node(data)
            pt=pt.next
    return head

def print_ll(head):
    ptr=head
    while ptr:
        print(ptr.val,"-",end="")
        ptr=ptr.next
    print()

head1=create_link_list([1,2,3])
head2=create_link_list([5,6,7,8])
print_ll(head1)
print_ll(head2)
head3=add_forward(head1,head2)
print_ll(head3)
