def solver():    
    n=int(input())
    arr=list(map(int,input().split()))
    total=sum(arr)
    if total%2!=0:
        print('NO')
        return
    total=total//2+1
    dp=[[False for _ in range(n)] for _ in range(total)]

    for i in range(total):
        dp[i][0]= True if i==arr[0] else False
    for j in range(n):
        dp[0][j]=True

    for i in range(1,total):
        for j in range(1,n):
            if i-arr[j]>=0:
                dp[i][j]=dp[i][j-1] or dp[i-arr[j]][j-1]
            else:
                dp[i][j]=dp[i][j-1]

    print('YES' if dp[total-1][n-1] else 'NO')



t=int(input())
for i in range(t):
    solver()
