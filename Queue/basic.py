import collections

class Queue:
    def __init__(self):
        self.q=collections.deque([])

    def push(self,item):
        self.q.append(item)

    def pop(self):
        return self.q.popleft() #O(k) hence its better to use dequeue

    def peek(self):
        return self.q[0]

    def isEmpty(self):
        if not self.q:
            return True
        else:
            return False

s= Queue()
s.push(5)
s.push(6)
s.push(7)

while not s.isEmpty():
    print(s.pop())