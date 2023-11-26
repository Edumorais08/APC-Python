n = float(input())
l = float(input())
qa = int(input())
custo = (n*l*1.025)
ordem = 1
while qa > 0:
  print('Lote: {} - Total da venda: R$ {:.2f} '.format((ordem), float(custo)))
  qa = qa-1
  ordem = ordem + 1
