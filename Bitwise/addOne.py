def add_one(x):
    m=1
    while(x&m):
        x=x^m
        m=m<<1

    x=x^m
    return x

print(add_one(102))
print(add_one(103))