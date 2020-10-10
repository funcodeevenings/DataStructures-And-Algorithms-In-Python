#dictionary approach
def has_unique_chars(str):
    hash={}
    for c in str:
        if c in hash:
            return False
        else:
            hash[c]=True
    return True

# set approach
def has_unique_chars_set(str):
    hash=set()
    for c in str:
        if c in hash:
            return False
        else:
            hash.add(c)
    return True

# bitwise approach
def has_unique_chars_int(str):
    num=0
    for c in str:
        c_num=ord(c)-ord('a')
        c_num = 1<<c_num
        if num & c_num >=c_num:
            return False
        else:
            num=num|c_num
    return True

inp=["abc","abcda","abxztyy"]
for i in inp:
    print(has_unique_chars(i),has_unique_chars_set(i),has_unique_chars_int(i))