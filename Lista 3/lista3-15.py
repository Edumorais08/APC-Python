n = int(input())
vetorx = []
vetory = []
vetorz = []

while n>0:
    x,y,z = map(int,input().split())
    vetorx.append(x)
    vetory.append(y)
    vetorz.append(z)
    n -= 1

somax = sum(vetorx)
somay = sum(vetory)
somaz = sum(vetorz)

if somax==0 and somay==0 and somaz==0:
    print('ESTACIONARIO')
else:
    print('MOVIMENTO')