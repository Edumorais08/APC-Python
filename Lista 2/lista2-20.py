def EhRetangulo(a,b,c):
    maior = max(a,b,c)
    valores = [a,b,c]
    sorteados = sorted(valores)
    menor1 = sorteados[0]
    menor2 = sorteados[1]
    if (maior)**2 == (menor1)**2 + (menor2)**2:
        return '1'
    else:
        return '0'
    

