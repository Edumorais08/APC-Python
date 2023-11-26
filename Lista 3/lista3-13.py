lista = []
ntermos = 0

while True:
    x = int(input())
    if x == -1:
        break
    valor = 1/x
    lista.append(valor)


soma = sum(lista)
ntermos = len(lista)
media = int(ntermos/soma)
print(media)
