def concatenar(a,b):
  soma = a+b
  print(soma)
  return soma


  
def repetir(a,c):
    c = int(c)
    mult = a*c
    print(mult)
    return mult

def ambos(a,b,c):
    c = int(c)
    ambos = (a+b)*c
    print(ambos)

a,b,c = input().split()    
concatenar(a,b)
repetir(a,c)
ambos(a,b,c)