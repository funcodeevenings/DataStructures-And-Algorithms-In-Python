import heapq

def heap_sort(arr):
    h=[]
    for val in arr:
        heapq.heappush(h,val)
    return [heapq.heappop(h) for i in range(len(h))]



arr=[5,9,125,34,6,45,12]
print(heap_sort(arr))