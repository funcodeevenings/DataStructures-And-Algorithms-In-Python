class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

def is_pallindrome(head):
    return is_pallindrome_util([head],head)

def is_pallindrome_util(left,right):
    if not right:
        return True

    isp = is_pallindrome_util(left,right.next)
    if not isp:
        return False
    
    isp1= left[0].val == right.val
    left[0] = left[0].next

    return isp1


def _is_pallindrome(head):
    if not head:
        return False
    if not head.next:
        return True
    p1=head
    p2=head
    prev_p2=None
    while p1 and p2:
        p3=p2.next
        if p1.next==None:
            return compare(prev_p2,p3)

        if not p1.next.next:
            p2.next=prev_p2
            return compare(p2,p3)
        
        p2.next=prev_p2
        prev_p2=p2
        p2=p3
        p1=p1.next.next
        
def _compare(head1,head2):
    p1,p2=head1,head2
    while p1 and p2:
        if p1.val != p2.val:
            return False
        p1,p2=p1.next,p2.next
    if p1 or p2:
        return False
    return True

l1 = None
l2= Node('a') #a
l3= Node('a') #ab
l3.next= Node('b')
l4= Node('a') #aa
l4.next= Node('a')
l5= Node('a') #aab
l5.next= Node('a')
l5.next= Node('b')
l6= Node('a') #aba
l6.next= Node('b')
l6.next= Node('a')
l7= Node('a') #abab
l7.next= Node('b')
l7.next= Node('a')
l7.next= Node('b')
l8= Node('a') #abba
l8.next= Node('b')
l8.next= Node('b')
l8.next= Node('a')


print('l1',is_pallindrome(l1))
print('l2',is_pallindrome(l2))
print('l3',is_pallindrome(l3))
print('l4',is_pallindrome(l4))
print('l5',is_pallindrome(l5))
print('l6',is_pallindrome(l6))
print('l7',is_pallindrome(l7))
print('l8',is_pallindrome(l8))