#code
mod=10**9+7

def sol():
    n = int(input())
    print(fib[n])
    
    
fib = [ 0 for _ in range(101)]
fib[1]=2
fib[2]=3
for i in range(3,101):
    fib[i]=(fib[i-1]%mod+fib[i-2]%mod)%mod
    
t=int(input())
for i in range(t):
    sol()   