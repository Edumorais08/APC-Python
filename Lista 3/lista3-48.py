jogo = input()
vantagem_corinthians = 0
vantagem_sp = 0
zeros = []
uns = []
soma_de_zeros = []
soma_de_uns = []
c = len(jogo) - 1

for n in jogo:
    if n == '1' :
        somax0 = ''.join(zeros)
        soma_de_zeros.append(somax0)
        zeros = []
    if n == '0':
        zeros.append(n)

for n in jogo:
    if n == '0' :
        somax1 = ''.join(uns)
        soma_de_uns.append(somax1)
        uns = []
    if n == '1':
        uns.append(n)

if jogo[c] == '1':
  somax1 = ''.join(uns)
  soma_de_uns.append(somax1)
if jogo[c] == '0':
   somax0 = ''.join(zeros)
   soma_de_zeros.append(somax0)

for i in soma_de_zeros:
  if len(i)>=7:
    vantagem_corinthians += 1

for i in soma_de_uns:
  if len(i)>=7:
    vantagem_sp += 1

if vantagem_corinthians==vantagem_sp and vantagem_sp>0:
  print( 'JOGO PESADO')
elif vantagem_corinthians==vantagem_sp and vantagem_sp==0:
  print('BORA UM VIRTUAL NO CODEFORCES')
elif vantagem_sp > vantagem_corinthians:
  print('VAMO TRICOLOR')
else:
  print('VAI TIMAO')