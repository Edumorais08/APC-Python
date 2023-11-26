a,b = map(int,input().split())
a = str(a)
b = str(b)

n = len(b)
x = len(a) - n
ultdigitos = a[x:]

if b == ultdigitos:
    print('ta dentro!!!')
else:
    print('ta fora...')
