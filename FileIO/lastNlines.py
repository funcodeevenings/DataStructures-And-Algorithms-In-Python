def tail(file, n=1, bs=1024):
    f = open(file)
    f.seek(0,2)
    l = 1
    B = f.tell()
    while n >= l and B > 0:
            block = min(bs, B)
            B -= block
            f.seek(B, 0)
            l += f.read(block).count('\n')
    f.seek(B, 0)
    l = min(l,n)
    lines = f.readlines()[-l:]
    f.close()
    return lines

n = int(input())
lines = tail("abc.txt",n)
print(lines)