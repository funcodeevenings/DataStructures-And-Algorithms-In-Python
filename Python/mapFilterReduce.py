# Map
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(items,squared)

#Filter
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(number_list,less_than_zero)

#Reduce
from functools import reduce
product = reduce((lambda x, y: x * y), items)
print(items,product)