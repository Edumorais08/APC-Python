N = int(input())
tempos = list(map(int,input().strip().split()))[:N]
tam = len(tempos)
maior = max(tempos)
i=0
lista = []

while tam>0:
    x = tempos[i]
    dif = maior-x
    lista.append(dif)
    tam -= 1
    i += 1

result = ' '.join(map(str,lista))
print(result)