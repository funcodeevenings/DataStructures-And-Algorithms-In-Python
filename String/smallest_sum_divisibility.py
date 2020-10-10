def create_string(num):
    if num==0:
        return 0
    nines = num//9
    rem = num%9
    digits = nines+rem
    if rem:
        st = str(rem)
    else:
        st = ''

    st = st + nines*str('9')
    st = st + num*str('0')
    return st

print(create_string(20))
print(create_string(5))
print(create_string(0))
