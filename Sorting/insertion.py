def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if a[j+1]<a[j]:
                a[j+1],a[j]=a[j],a[j+1]
            else:
                break

arr=[64,34,45,78,34,23,67,83]
insertion_sort(arr)
print(arr)