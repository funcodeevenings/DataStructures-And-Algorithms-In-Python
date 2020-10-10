import collections

class Stack:
    def __init__(self):
        self.stack=collections.deque([])

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

def sol():
    st=input()
    l=len(st)
    if l==1:
        print('0')
        return
    s = Stack()
    dp = [0 for _ in range(l+1)]
    for i,c in enumerate(st):
        if c=='(':
            s.push(('(',i))
            dp[i+1]=0
        else:
            if s.isEmpty()==False and s.peek()[0] == '(':
                sym,ind= s.pop()
                x=i-ind+1
                dp[i+1]=dp[i+1-x]+x
            else:
                s.push((')',-1))
            
                
    print(max(dp))
            
        
        
    
t=int(input())
for i in range(t):
    sol()