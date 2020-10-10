"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers.
By convention, 1 is included.
Given a number n, the task is to find n’th Ugly number.
"""
tests=int(input())
ugly = [1]
id1=id2=id3=0
mul2,mul3,mul5=2,3,5
while tests:
    tests = tests-1
    n=int(input())
    if len(ugly) >=n:
        print(ugly[n-1])
    else:
        index=len(ugly)
        while index <=n:
            num=min(mul2,mul3,mul5)
            ugly.append(num)
            if num==mul2:
                id1=id1+1
                mul2=ugly[id1]*2
            if num==mul3:
                id2=id2+1
                mul3=ugly[id2]*3
            if num==mul5:
                id3=id3+1
                mul5=ugly[id3]*5
            index=index+1
        
        print(ugly[n-1])



