def cut_strings_pallindrom(A,B):
    l=min(len(A),len(B))
    for i in range(l):
        st=A[0:i+1]+B[i+1:]
        if is_pallin(st):
            return True
    return False

def is_pallin(st):
    f,l=0,len(st)-1
    while(f<l):
        if st[f]!=st[l]:
            return False
        f=f+1
        l=l-1
    
    return True

A="abc"
B="def"
print(cut_strings_pallindrom(A,B))
