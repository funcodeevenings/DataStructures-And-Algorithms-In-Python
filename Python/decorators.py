#code
t=int(input())
while t:
    t=t-1
    n=int(input())
    l = [int(x) for x in input().split()]
    min,max=int(l[0]),int(l[0])
    ind1=0
    ind2=0
    profit=0
    flag=0
    for i,x in enumerate(l[1:]):
        exp=int(x)-min
        if exp<profit and ind1<ind2:
            flag=1
            profit=0
            print('(',end='')
            print(ind1,ind2,end='')
            print(')',end=' ')
            ind1=ind2=i+1
            min=max=int(x)
        elif exp<profit:
            profit=0
            ind1=ind2=i+1
            min=max=int(x)
        else:
            profit=exp
            ind2=i+1
            max=int(x)
    if exp>0 and ind1<ind2:
        flag=1
        print('(',end='')
        print(ind1,ind2,end='')
        print(')',end='')
        
    if flag==0:
        print("No Profit",end='')
    
    print()