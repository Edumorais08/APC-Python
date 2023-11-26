#resto de divisão
def age(days):
  import math
  anos = days / 360
  meses = (days % 360) / 30
  days = (days % 360) % 30
  print(math.floor(anos),math.floor(meses),math.floor(days)) 


d1,d2,d3 = map(int,input().split())
age(d1)
age(d2)
age(d3)
