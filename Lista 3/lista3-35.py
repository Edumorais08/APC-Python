def soma_aninhada(lista):
    soma = 0
    for i in lista:
        if isinstance(i, list):
            soma+=soma_aninhada(i)
        if isinstance(i, int):
            soma+=i
    return soma