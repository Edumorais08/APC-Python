n = int(input())
lista=[]

while n>0:
    a = int(input())
    lista.append(a)
    n -= 1

ordem = sorted(lista)
maior = max(ordem)
menor = min(ordem)

print(f'Menor: {menor}')
print(f'Maior: {maior}')
