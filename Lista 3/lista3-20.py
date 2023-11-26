N = int(input())
tempos = list(map(int,input().strip().split()))[:N]
tam = len(tempos)
menor = min(tempos)
i=0
lista = []

while tam>0:
    x = tempos[i]
    dif = x-menor
    lista.append(dif)
    tam -= 1
    i += 1

result = ' '.join(map(str,lista))
print(result)
