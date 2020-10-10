def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j

        arr[min_index],arr[i] = arr[i],arr[min_index]

arr=[64,34,45,78,34,23,67,83]
selection_sort(arr)
print(arr)
    
