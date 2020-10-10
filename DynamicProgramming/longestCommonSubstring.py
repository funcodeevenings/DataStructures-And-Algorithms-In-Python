def sol():
    n,m=map(int,input().split())
    x=input()
    y=input()
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    max=0
    for a,j in enumerate(x):
        for b,i in enumerate(y):
            if i==j:
                dp[b+1][a+1]=1+dp[b][a]
                if max<dp[b+1][a+1]:
                    max=dp[b+1][a+1]
    print(max)
    
t=int(input())
for i in range(t):
    sol()