def quick_sort(arr,l,r):
    if l<r:
        p = partition(arr,l,r)
        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,r)

def partition(arr,l,h):
    i=l-1
    pivot=arr[h]
    for j in range(l,h):
        if arr[j]<=pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1

arr=[64,34,45,78,34,23,67,83]
quick_sort(arr,0,7)
print(arr)  
