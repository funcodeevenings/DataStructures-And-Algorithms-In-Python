#code
t=int(input())
n=101
dp = [1 for _ in range(n)]

for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]
while t:
    t=t-1
    n=int(input())
    for i in range(n):
        print(dp[i],end=' ')
    print()
    