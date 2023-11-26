def converte(X):
   resultado = (X * 9/5) + 32
   print('{:.1f}'.format(resultado))

X = float(input())
converte(X)