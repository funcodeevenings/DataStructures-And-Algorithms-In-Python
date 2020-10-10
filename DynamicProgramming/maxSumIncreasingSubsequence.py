#code
def solution():
    n=int(input())
    a=list(map(int,input().split()))
    dp=[x for x in a]
    
    for i in range(1,n):
        for j in range(i):
            if a[i]>a[j]:
                dp[i]=max(dp[i],a[i]+dp[j])
            
    print(max(dp))
    
t=int(input())
for i in range(t):
    solution()