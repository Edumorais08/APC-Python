numeros = list(map(int,input().split()))
N = len(numeros)
mediax = sum(numeros)/N
lista = []

for xi in numeros:
    termo1 = mediax - xi
    termo2 = termo1**2
    lista.append(termo2)

resultado1 = sum(lista)/N

import math
resultado2 = math.sqrt(resultado1)

print('{:.1f}'.format(resultado1))
print('{:.1f}'.format(resultado2))