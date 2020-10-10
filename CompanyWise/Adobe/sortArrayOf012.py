#code
t = int(input())
while t:
    t=t-1
    n=int(input())
    l=list(map(int,input().split()))
    c0,c1,c2=0,0,0
    for x in l:
        if x==0:
            c0=c0+1
        elif x==1:
            c1=c1+1
        elif x==2:
            c2=c2+1
    
    l2 = [ 0 for _ in range(c0)]
    l2.extend([1 for _ in range(c1)])
    l2.extend([2 for _ in range(c2)])
    
    print(" ".join(str(x) for x in l2))