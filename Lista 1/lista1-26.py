def peso_ideal(altura):
  print('{:.2f}'.format(72.7 * altura - 58), '{:.2f}'.format(62.1 * altura - 44.7))

altura = float(input())
peso_ideal(altura)