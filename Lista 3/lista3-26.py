pontos = list(map(int,input().split()))

x = min(pontos)
pontos.remove(x)
n = len(pontos)

ordem = sorted(pontos)
ordenado = []
i = n-1

while n>0:
    y = pontos[i]
    ordenado.append(y)
    n -= 1
    i -= 1


result = ' '.join(map(str,ordenado))
print(result)