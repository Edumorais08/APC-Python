n = int(input())
while n>0:
    j1,j2 = input().split()
    if j1 == j2:
        print('Empate.')
    elif j1=='tesoura' and j2=='papel' or j1=='papel' and j2=='pedra'or j1=='pedra' and j2=='tesoura':
        print('Jogador 01 venceu.')
    else:
        print('Jogador 02 venceu.')

    n -= 1