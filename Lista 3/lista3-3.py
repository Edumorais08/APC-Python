amigos , preço = map(int,input().split())
dinheiro_total = []

while amigos > 0:
    dinheiro = int(input())
    dinheiro_total.append(dinheiro)
    amigos -= 1

soma = sum(dinheiro_total)
ntermos = len(dinheiro_total)
media = int(soma / ntermos)

print(f'media: {media}')
if media >= preço:
    print('o rock reinara mais uma vez')
else:
    print('rockeiros trabalhando ja')
