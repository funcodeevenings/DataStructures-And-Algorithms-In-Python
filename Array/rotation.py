import copy
print('Enter the list')
l = [int(x) for x in input().split()]
d = int(input("Enter the number"))

# right rotate
def right_rotate(item_list,number):
    arr = item_list
    d = number
    while(d):
        d=d-1
        x = arr.pop(0)
        arr.append(x)
    print(arr)

right_rotate(l,d)

# left rotate
def left_rotate(item_list,number):
    arr = item_list
    d=number
    n=arr.__len__()
    while(d):
        d=d-1
        x=arr.pop(n-1)
        arr.insert(0,x)
    print(arr)

left_rotate(l,d)