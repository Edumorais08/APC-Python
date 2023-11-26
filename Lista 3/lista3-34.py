lista = list(map(int,input().split()))
tam = len(lista)
x = lista[0]
vetores = [x]
i = 1
y = 0

while i<tam:

    w = lista[i]
    z = vetores[y]
    sum = w + z
    vetores.append(sum)
    i += 1
    y += 1

result = ' '.join(map(str,lista))
result2 = ' '.join(map(str,vetores))

print(result2)
print(result)