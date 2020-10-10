def pair_sum(item_list,sum):
    d = {}
    for i in item_list:
        if d.__contains__(sum-item_list[i]):
            return(True,i,d[sum-item_list[i]])
        else:
            d[item_list[i]] = i
    return False

print(pair_sum([1,2,3,4,5,6,7,8,9],15))