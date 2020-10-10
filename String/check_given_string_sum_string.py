import re

def solve(inp):
    lis = re.findall("\d+",inp)
    ans=0
    for x in lis:
        ans=ans+int(x)
    
    return ans

print(solve("1abc23"))
print(solve("geeks4geeks"))
print(solve("1abc2x30yz67"))
print(solve("123abc"))