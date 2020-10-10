import keyword

# if keyword.iskeyword("hello"):
#     print("yes")
# else:
#     print("no")

# if keyword.iskeyword("if"):
#     print("yes")
# else:
#     print("no")


# print (False == 0)
# print (True == 1)
 
# print (True + True + True)
# print (True + False + False)

# Python code to demonstrate working of
# global and non local
 
#initializing variable globally
a = 10
 
# used to read the variable
def read():
    print (a)
 
# changing the value of globally defined variable
def mod1():
    global a 
    a = 5

 
# reading initial value of a
# prints 10
read()
 
# calling mod 1 function to modify value
# modifies value of global a to 5
mod1()
 
# reading modified value
# prints 5
read()
 

# reading modified value
# again prints 5
read()
 
# demonstrating non local 
# inner loop changing the value of outer a
# prints 10
print ("Value of a using nonlocal is : ",end="")
def outer():
    a = 5
    def inner():
        nonlocal a 
        a = 10
    inner()
    print (a)
 
outer()
 
# demonstrating without non local 
# inner loop not changing the value of outer a
# prints 5
print ("Value of a without using nonlocal is : ",end="")
