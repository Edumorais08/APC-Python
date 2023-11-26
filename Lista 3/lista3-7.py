n = int(input())
lista = []

if n>0:
    while n>0:
        nd = n%10
        nd = str(nd)
        lista.append(nd)
        n = n//10

elif n<0:
    n = n*(-1)
    lista.append('-')
    while n>0:
        nd = n%10
        nd = str(nd)
        lista.append(nd)
        n = n//10


delimitador = ''
resultado = delimitador.join(lista)
resultado = int(resultado)
print(resultado)

