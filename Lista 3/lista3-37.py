def remover_zeros(s):
    n = len(s)
    inicio = False
    zeros = 0
    resposta = 0

    for i in range(n):
        if s[i] == '1':
            if not inicio:
                inicio = True
            else:
                resposta += zeros
            zeros = 0
        elif inicio:
            zeros += 1

    return resposta
n = int(input())
for _ in range(n):
    s = input()
    resposta = remover_zeros(s)
    print(resposta)