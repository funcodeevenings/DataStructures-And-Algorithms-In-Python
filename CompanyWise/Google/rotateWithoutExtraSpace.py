# If the array is 
# 1 2 3 4 5 6 7 8 9
# Then the rotated array becomes: 
# 7 4 1 8 5 2 9 6 3
#rotate by 90degree clockwise without extra space

# Function to rotate the matrix 
# 90 degree clockwise 
def rotate90Clockwise(A): 
    N = len(A[0]) 
    for i in range(N // 2): 
        for j in range(i, N - i - 1): 
            temp = A[i][j] 
            A[i][j] = A[N - 1 - j][i] 
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j] 
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i] 
            A[j][N - 1 - i] = temp 
  
# Function to print the matrix 
def printMatrix(A): 
    N = len(A[0]) 
    for i in range(N): 
        print(" ".join(A[i]), end=" ")
    print() 
  
# Driver code 
t = int(input())
while(t):
    t=t-1
    n=int(input())
    A1d =  [x for x in input().split(" ")]
    A = []
    for i in range(0,n*n,n):
        A.append(A1d[i:i+n])
    print(A)
    rotate90Clockwise(A) 
    printMatrix(A) 
  
# This code was contributed  
# by pk_tautolo 