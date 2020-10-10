print('Enter the list')
l = [int(x) for x in input().split()]
d = int(input("Enter the number"))
arr = l
n = arr.__len__()
print("n=",n)
print(arr)
arr.reverse()
print(arr)
rot = arr[n-d-1::-1]
rot.extend(arr[:n-d-1:-1])
print(rot)