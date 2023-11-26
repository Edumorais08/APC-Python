n = int(input())
while n>0:
    codigo = input()
    codigo = list(codigo)
    ulttermo = len(codigo)
    letras_maiusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                         'W', 'X', 'Y', 'Z']
    nsomas = []
    soma_feita = []
    letras = []
    for i in codigo:
      if i in letras_maiusculas :
        letras.append(i)
        conta = ''.join(nsomas)
        soma_feita.append(conta)
        nsomas = []
      if i not in letras_maiusculas:
        nsomas.append(i)
    conta = ''.join(nsomas)
    soma_feita.append(conta)
    multiply = []
    contador = 1
    for i in letras:
      multiply_conta = i * int(soma_feita[contador])
      multiply.append(multiply_conta)
      contador += 1
    print(''.join(multiply))
    n -= 1