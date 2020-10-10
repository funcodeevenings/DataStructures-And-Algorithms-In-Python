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

class popHeavyQueue:
    def __init__(self):
        self.s1 = Stack() #push
        self.s2 = Stack() #pop

    def push(self,item):
        self.s1.push(item)

    def pop(self):
        if self.s1.isEmpty() and self.s2.isEmpty():
            return
        elif not self.s2.isEmpty():
            return self.s2.pop()
        else:
            x=self.s1.pop()
            while not self.s1.isEmpty():
                self.s2.push(x)
                x=self.s1.pop()
            return x
    
    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()

s= popHeavyQueue()
s.push(5)
s.push(6)
s.push(7)

while not s.isEmpty():
    print(s.pop())