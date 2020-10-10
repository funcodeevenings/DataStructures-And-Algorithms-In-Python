def r_binary_search(item_list,item):
    first=0
    last = len(item_list)-1
    found = False
    while(first<=last and not found):
        mid = (first+last)//2
        if item_list[mid] == item:
            found = True
            return (found,mid)
        elif item_list[first] < item_list[mid]:
            if item_list[first] <= item < item_list[mid] :
                last = mid-1
            else:
                first = mid+1
        else:
            if item_list[mid] < item <= item_list[last] :
                first = mid+1
            else:
                last = mid-1
    return found
	
print(r_binary_search([6,7,8,9,10,1,2,3,5], 6)) #right-rotated


print(r_binary_search([9,10,1,2,3,5,6,7,8], 5)) #left-rotated
