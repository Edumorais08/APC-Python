def Ordena(a,b,c):
    maior = max(a,b,c)
    valores = [a,b,c]
    sorteados = sorted(valores)
    menor1 = sorteados[0]
    menor2 = sorteados[1]
    return '({}, {}, {})'.format(menor1,menor2,maior)

print(Ordena(1,37,12))