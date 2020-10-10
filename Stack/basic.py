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

s= Stack()
s.push(5)
s.push(6)
s.push(7)

while not s.isEmpty():
    print(s.pop())