import collections

class Queue:
    def __init__(self):
        self.q=collections.deque([])

    def push(self,item):
        self.q.append(item)

    def pop(self):
        return self.q.popleft() #O(1) hence its better to use dequeue

    def peek(self):
        return self.q[0]

    def isEmpty(self):
        if not self.q:
            return True
        else:
            return False

class PopHeavyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.toUse = self.q1
        self.notToUse = self.q2

    def push(self,item):
        self.toUse.push(item)

    def pop(self):
        if self.toUse.isEmpty():
            return
        else:
            x = self.toUse.pop()
            while not self.toUse.isEmpty():
                self.notToUse.push(x)
                x=self.toUse.pop()
            temp=self.toUse
            self.toUse=self.notToUse
            self.notToUse=temp
            return x
    
    def isEmpty(self):
        return self.toUse.isEmpty()

class PushHeavyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.toUse = self.q1
        self.notToUse = self.q2

    def pop(self):
        if self.notToUse.isEmpty():
            return
        else:
            return self.notToUse.pop()

    def push(self,item):
        self.toUse.push(item)
        while not self.notToUse.isEmpty():
            x=self.notToUse.pop()
            self.toUse.push(x)
        temp=self.toUse
        self.toUse=self.notToUse
        self.notToUse=temp
        
    
    def isEmpty(self):
        return self.notToUse.isEmpty()

s = PushHeavyStack()
s.push(5)
s.push(6)
s.push(7)
print(s.pop())
s.push(5)
s.push(6)
s.push(7)

while not s.isEmpty():
    print(s.pop())