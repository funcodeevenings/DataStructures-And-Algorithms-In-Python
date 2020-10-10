#code
def sol():
    n=int(input())
    prices=list(map(int,input().split()))
    bd,d,sd=0,0,0
    price=prices[d]
    flag=0
    d=1
    while d<n:
        if prices[d]>price:
            flag=1
            sd=sd+1
        else:
            if sd>bd:
                print('(',bd,' ',sd,')',sep='',end=' ')
                
            bd,sd=d,d
                
        price=prices[d]
        d=d+1
    
    if flag==0:
        print("No Profit")
    else:
        if sd>bd:
                print('(',bd,' ',sd,')',sep='',end=' ')
        print()
        
t=int(input())
while t:
    t=t-1
    sol()
        