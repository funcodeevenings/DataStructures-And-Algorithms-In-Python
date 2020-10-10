#code
def solver():
    n,m=map(int,input().split())
    a=input()
    b=input()
    print(a,b,n,m)
    dp=[[ 0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if b[i-1]==a[j-1]:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],1+dp[i-1][j-1])
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
    print(dp[m][n])
    
t=int(input())
for i in range(t):
    solver()