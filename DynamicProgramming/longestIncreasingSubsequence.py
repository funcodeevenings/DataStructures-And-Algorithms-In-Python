t = int(input())
while t:
    t=t-1
    l = [int(x) for x in input().split()]
    n=len(l)
    lis = [1 for x in l]
    m=len(lis)
    maxlen=1
    for i in range(1,n):
        j=0
        while j<i:
            if l[j] < l[i]:
                lis[i] = max(lis[j]+1, lis[i])
            j=j+1
        if l[i]>maxlen:
            maxlen=l[i]
    print(maxlen)