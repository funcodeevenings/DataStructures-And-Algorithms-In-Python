def mat_bfs(mat,s):
    row,col=len(mat),len(mat[0])
    visited = [[False for i in range(col)] for j in range(row)]
    q=[(s,0)]
    found_d=False
    min=row*col
    while len(q)>0:
        ((i,j),count)=q.pop(0)
        visited[i][j]=True
        if i-1>=0:
            if mat[i-1][j]=='*' and visited[i-1][j]==False:
                q.append(((i-1,j),count+1))
                visited[i-1][j]=True
            elif mat[i-1][j]=='d':
                found_d=True
                min=count+1 if min>count+1 else min
        if i+1<row:
            if mat[i+1][j]=='*' and visited[i+1][j]==False:
                q.append(((i+1,j),count+1))
                visited[i+1][j]=True
            elif mat[i+1][j]=='d':
                found_d=True
                min=count+1 if min>count+1 else min
        if j-1>=0:
            if mat[i][j-1]=='*' and visited[i][j-1]==False:
                q.append(((i,j-1),count+1))
                visited[i][j-1]=True
            elif mat[i][j-1]=='d':
                found_d=True
                min=count+1 if min>count+1 else min
        if j+1<col:
            if mat[i][j+1]=='*' and visited[i][j+1]==False:
                q.append(((i,j+1),count+1))
                visited[i][j+1]=True
            elif mat[i][j+1]=='d':
                found_d=True
                min=count+1 if min>count+1 else min
    
    if found_d==True:
        return min
    else:
        return -1

def shortest_dist(mat):
    for i,row in enumerate(mat):
        for j,cell in enumerate(row):
            if cell=='s':
                s=(i,j)

    return mat_bfs(mat,s)

mat = [ ['0', '*', '0', 's'],
        ['*', '0', '*', '*'],
        ['0', '*', '*', '*'],
        ['d', '*', '*', '*']
    ]

print(shortest_dist(mat))