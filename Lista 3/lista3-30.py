def atualizaMatriz(matriz, lin, col, tipo):
    matriz[lin][col] = tipo
    return matriz

def imprimeJogo(matriz):
    for linha in matriz:
        print(''.join(linha))

def jogoTerminou(matriz):
    for linha in matriz:
        if linha[0] == linha[1] == linha[2] != ' - ':
            return 1

    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna] != ' - ':
            return 1

    if matriz[0][0] == matriz[1][1] == matriz[2][2] != ' - ' or matriz[0][2] == matriz[1][1] == matriz[2][0] != ' - ':
        return 1

    if all(item != ' - ' for linha in matriz for item in linha):
        return 2

    return 0


matriz = [[' - ', ' - ', ' - '],
          [' - ', ' - ', ' - '],
          [' - ', ' - ', ' - ']]

jogador = ' X '
estado = True

while estado:
    imprimeJogo(matriz)
    result = jogoTerminou(matriz)

    if result == 1:
        print('Ganhou')
        estado = False
        break
    elif result == 2:
        print('Empate')
        estado = False
        break

    jogada = list(map(int, input().split()))

    matriz = atualizaMatriz(matriz, jogada[0], jogada[1], jogador)

    jogador = ' O ' if jogador == ' X ' else ' X '