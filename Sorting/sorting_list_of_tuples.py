l=[(1,'a'),(10,'b'),(5,'c'),(4,'d')]
#sorting by first element
l.sort()
print(l)
#sorting by second element
sorted(l,key=lambda x:x[1])
print(l)