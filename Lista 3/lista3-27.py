'''Cada posição da lista desenho representa um dos estados da forca'''
desenhos = ['''
 +---+
 |   |
     |
     |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
     |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
========
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
========
''', '''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
========
''']

def STR (lista):
  STRlista = ''

  for i in lista:
    STRlista+=f'{i}'

  return STRlista

palavra = input('Digite a palavra secreta: ')
palavraLista = list(palavra)

def remover_repeticao(palavra):
    l = []
    for i in palavra:
        if i not in l:
            l.append(i)
    l.sort()
    return l

letras_dif = remover_repeticao(palavra)
acertos_nec = len(letras_dif)

jogo = True

desenho_atual = 0
erros = 0
acertos = 0

palavra_formada = []

letras_chutadas = []

for i in palavra:
    palavra_formada.append(f'_ ')

print(f'''
 +---+
 |   |
     |
     |
     |
     |
========

{STR(palavra_formada)}''')
while jogo == True:
    letra = input('Digite uma letra: ')
    if letra not in letras_chutadas:
      letras_chutadas.append(letra)
    else:
      acertos-=1

    if letra in letras_dif:
      acertos+=1

      cont = -1
      for i in palavra:
        cont+=1
        if i == letra:
          palavra_formada[cont] = f'{letra} '

      print(f'''{desenhos[desenho_atual]}
{STR(palavra_formada)}''')
    else:
      erros+=1
      desenho_atual +=1
      print(f'''{desenhos[desenho_atual]}
{STR(palavra_formada)}''')

    if acertos == acertos_nec:
      print(f'Sim! A palavra secreta eh "{palavra}"')
      jogo = False
      break
    elif erros == 6:
      print('Voce teve muitas oportunidades e perdeu!')
      jogo = False
      break