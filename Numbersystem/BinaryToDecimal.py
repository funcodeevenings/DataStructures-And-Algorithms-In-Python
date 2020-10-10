binary = input("Binary Number =")
mul=1
number=0
for i in range(len(binary)-1,-1,-1):
    number=number+(ord(binary[i])-ord('0'))*mul
    mul=mul*2

print(number)

binary = int(input("Binary Number ="))
mul=1
number=0
while binary:
    number=number+(binary%10)*mul
    mul=mul*2
    binary=binary//10

print(number)