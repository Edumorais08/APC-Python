a,b = map(int,input().split())
valores = [a,b]
ordem = sorted(valores)
n = max(ordem)
n -= 1
while n > 2:
    if a%n==0 and b%n==0:
        break
    n -= 1

if a%n==0 and b%n==0:
    print('Nao sao co-primos!')
else:
    print('Sao co-primos.')