import math

def solver():
    n=int(input())
    a=list(map(int,input().split()))
    dp=[ math.inf for _ in range(n)]
    dp[0]=0
    
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if i-j <=a[j]:
                dp[i] = min(dp[i],1+dp[j])
                
    if dp[n-1]==math.inf:
        print('-1')
    else:
        print(dp[n-1])
        
t=int(input())
for i in range(t):
    solver()
        