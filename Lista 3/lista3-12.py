lista = []
ntermos = 0

while True:
    x = int(input())
    if x == -1:
        break
    lista.append(x)


soma = sum(lista)
ntermos = len(lista)
media = soma//ntermos
print(media)


