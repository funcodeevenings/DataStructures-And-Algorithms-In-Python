def is_pallindrome(head):
	if head==None or head.next==None:
		return True

	len=find_len(head)
	rev_head,next_head=reverse_list(head,len//2)
	if len&1:
		non_rev_head=next_head.next
	else:
		non_rev_head=next_head
	is_equal=compare_link_list(rev_head,non_rev_head)
	head=reverse_first_and_append(rev_head,next_head)
	return is_equal
	
def reverse_list(head,len):
	prev=None
	ptr=head
	next=head.next
	while len:
		if not ptr:
			return None,None
		ptr.next=prev
		prev=ptr
		ptr=next
		next=ptr if ptr.next else None
		len=len-1
	
	return prev,ptr

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

def compare_link_list(head1,head2):
	pt1,pt2=head1,head2
	while pt1 and pt2:
		if pt1.val!=pt2.val:
			return False
	if pt1 or pt2:
		return False
	return True

def reverse_first_and_append(head1,head2):
    head=None
    prev=None
    ptr=head1
    


head1=create_link_list([1,2,3,2,1])
head2=create_link_list([1,2,3,3,2,1])

head1=create_link_list([1,4,3,2,1])
head2=create_link_list([1,2,5,3,2,1])