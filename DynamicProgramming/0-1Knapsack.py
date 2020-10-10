#code
def solver():
    n=int(input())
    W=int(input())
    val=list(map(int,input().split()))
    wt=list(map(int,input().split()))
    dp=[[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1,W+1):
            if j>=wt[i-1]:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1],val[i-1]+dp[i-1][j-wt[i-1]])
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                
    print(dp[n][W])
    
t=int(input())
for i in range(t):
    solver()
    