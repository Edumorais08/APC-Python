lista = list(map(int, input().split()))
tam = len(lista)
i = 0
w = tam-1
j = tam

while w>1:
    if lista[i] == lista[w]:
        break
    w -= 1


if j == 1:
    print('False')
elif lista[i] == lista[w]:
    print('True')
else:
    print('False')