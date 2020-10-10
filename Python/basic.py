import re

l = [1,2,3,4,5]
s= "Hello \nhow \nare you?"
a = s.split()
b = s.split(' ')
c = s.split(' ',2)
d = s.split('\n')
print(a,b,c,d)

a = re.sub(r"a.*e",'au',s)
print(a)

# Program to handle multiple errors with one except statement
try : 
    a = 3
    if a < 4 :
 
        # throws ZeroDivisionError for a = 3 
        b = a/(a-3)
     
    # throws NameError if a >= 4
    print("Value of b = ", b)
 
# note that braces () are necessary here for multiple exceptions
except(ZeroDivisionError, NameError):
    print("\nError Occurred and Handled")
