n = int(input())

while n>0:
    l, r, s = input().split()
    l = int(l)
    r = int(r)+1
    result = (s[l:r])
    print(result)
    n -= 1