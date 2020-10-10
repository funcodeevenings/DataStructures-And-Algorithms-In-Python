import math

t=int(input())
while t:
    t=t-1
    n=int(input())
    a=[int(x) for x in input().split()]
    sum=0
    max=-1*math.inf
    for i in a:
        sum = sum+i
        if sum>max:
            max=sum
        if sum<0:
            sum=0
    print(max)
        