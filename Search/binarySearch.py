def binary_search(item_list,item):
    first=0
    last = len(item_list)-1
    found = False
    while(first<=last and not found):
        mid = (first+last)//2
        if item_list[mid] == item:
            found = True
            return mid
        elif item_list[mid] < item:
            first = mid+1
        else:
            last = mid-1
    return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))