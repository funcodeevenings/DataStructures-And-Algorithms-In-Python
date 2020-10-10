#code
def sol():
    m=int(input())
    coins=list(map(int,input().split()))
    n=int(input())
    dp=[[ 0 for _ in range(n+1)] for _ in range(m)]
    
    for i in range(m):
        dp[i][0]=1
        
    for i in range(m):
        for j in range(n+1):
            if j>=coins[i]:
                dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
            else:
                dp[i][j]=dp[i-1][j]
            
    print(dp[m-1][n])
    
t=int(input())
for i in range(t):
    sol()