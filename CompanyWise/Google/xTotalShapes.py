def bfs(i,j,visited,n,m):
    q = [(i,j)]
    while q:
        i,j=q.pop(0)
        if j+1<m and visited[i][j+1]==0 and M[i][j+1]=='X':
            q.append((i,j+1))
            visited[i][j+1]=1
        if i+1<n and visited[i+1][j]==0 and M[i+1][j]=='X':
            q.append((i+1,j))
            visited[i+1][j]=1
        if j-1>=0 and visited[i][j-1]==0 and M[i][j-1]=='X':
            q.append((i,j-1))
            visited[i][j-1]=1
        if i-1>=0 and visited[i-1][j]==0 and M[i-1][j]=='X':
            q.append((i-1,j))
            visited[i-1][j]=1


t = int(input())
while(t):
    t=t-1
    n,m=map(int,input().split(" "))
    M=input().split(" ")
    M = [list(x) for x in M]
    # count the connected components
    visited=[[ 0 for _ in range(m)] for _ in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and M[i][j]=='X':
                count=count+1
                visited[i][j]=1
                bfs(i,j,visited,n,m)
    print(count)
            

