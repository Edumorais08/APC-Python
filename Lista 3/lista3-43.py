n = int(input())

while n>0:
    l, r, s = input().split()
    l = int(l)
    r = int(r)+1
    T = (s[l:r])
    result = ''.join(reversed(T))
    print(result)
    n -= 1