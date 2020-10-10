n=int(input("n="))
primes=[True for i in range(4*n)]
for i in range(2,4*n):
    if primes[i]:
        x=2*i
        while x<4*n:
            primes[x]=False
            x=x+x

i,j=0,2
sum=0
while i<n:
    if primes[j]:
        sum=sum+j
        i=i+1
    j=j+1
print(sum)