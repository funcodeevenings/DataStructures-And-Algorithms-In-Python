import sys
  
# Function to left 
# rotate n by d bits 
def leftRotate(n, d): 
  
    # In n<<d, last d bits are 0. 
    # To put first 3 bits of n at  
    # last, do bitwise or of n<<d 
    # with n >>(INT_BITS - d) 
    INT_BITS = sys.getsizeof(n) 
    return (n << d)|(n >> (INT_BITS - d)) 
  
# Function to right 
# rotate n by d bits 
def rightRotate(n, d): 
  
    # In n>>d, first d bits are 0. 
    # To put last 3 bits of at  
    # first, do bitwise or of n>>d 
    # with n <<(INT_BITS - d)  
    INT_BITS = sys.getsizeof(n)
    all_set = 1
    x=INT_BITS
    while(x):
        all_set=all_set<<1
        all_set=all_set|1
        x=x-1
    return (n >> d)|(n << (INT_BITS - d)) & all_set
  
# Driver program to 
# test above functions  
n = 16
d = 2
  
print("Left Rotation of",n,"by"
      ,d,"is",end=" ") 
print(leftRotate(n, d)) 
  
print("Right Rotation of",n,"by"
     ,d,"is",end=" ") 
print(rightRotate(n, d)) 