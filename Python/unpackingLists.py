# A sample function that takes 4 arguments
# and prints the,
def fun(a, b, c, d):
    print(a, b, c, d)
 
# Driver Code
my_list = [1, 2, 3, 4]
 
# Unpacking list into four arguments
fun(*my_list)

def mySum(*args):
    sum = 0
    for i in range(len(args)):
        sum = sum + args[i]
    return sum
 
# Driver code
print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

# * -> unpack lists
# ** -> unpack dicts

# A Python program to demonstrate packing of
# dictionary items using **
def fun2(**kwargs):
 
    # kwargs is a dict
    print(type(kwargs))
 
    # Printing dictionary items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))
 
# Driver code
fun2(name="geeks", ID="101", language="Python")


print("Welcome to" , end = ' ') 
print("GeeksforGeeks", end = ' ')

print("Python" , end = '@') 
print("GeeksforGeeks")