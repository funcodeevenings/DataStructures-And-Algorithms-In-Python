arr = list(map(int,input().split()))
y=0
for x in arr:
   y=x^y 

print(y)