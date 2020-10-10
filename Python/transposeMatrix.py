
# m = [[1,2],[3,4],[5,6]]
# for row in m :
#     print(row)

# rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

# print("\n")
# for row in rez:
#     print(row)

#List Comprehension
a = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
c=[[j*2 for j in i] for i in a]
d=[[a[i][j]*2 for j in range(len(a[0]))] for i in range(len(a))]
e=[[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
print("c=",c)
print("d=",d)
print("e=",e)

# b = [[a[i][j]*2 for i in range(len(a))] for j in range(len(a[0]))]
# print(b)


matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]
for row in matrix:
    print(row)
print("\n")
t_matrix = zip(*matrix)
for row in t_matrix:
    print(row)


import numpy 
matrix=[[1,2,3],[4,5,6]]
print(matrix)
print("\n")
print(numpy.transpose(matrix))