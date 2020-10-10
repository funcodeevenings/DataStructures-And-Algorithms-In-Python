def merge_sort(arr,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(arr,l,m)
        merge_sort(arr,m+1,r)
        merge(arr,l,m,r)

def merge(arr,l,m,r):
    temp=[]
    a,b=l,m+1
    while a<=m and b<=r:
        if arr[a]<arr[b]:
            temp.append(arr[a])
            a=a+1
        else:
            temp.append(arr[b])
            b=b+1

    if a<=m:
        temp.extend(arr[a:m+1])
    if b<=r:
        temp.extend(arr[b:r+1])
    arr[l:r+1] = temp
    print("temp=",temp)


arr=[64,34,45,78,34,23,67,83]
merge_sort(arr,0,7)
print(arr)

