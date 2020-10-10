def remove_zeros(p):
    while(p[0]==0):
        p.pop(0)
    while(p[-1]==0):
        p.pop(-1)

p=[0,0,1,2,3,0,0]
remove_zeros(p)
print(p)