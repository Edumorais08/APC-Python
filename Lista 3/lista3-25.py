pontos = list(map(int,input().split()))
menor = min(pontos)
maior = max(pontos)
n = len(pontos)
pos_maior = 0
pos_menor = 0
i = 0

while n>0:
    x = pontos[i]
    if x == maior:
        pos_maior = i
    if x == menor:
        pos_menor = i
    n -= 1
    i += 1

print(menor, pos_menor)
print(maior, pos_maior)

result = ' '.join(map(str,pontos))
print(result)
