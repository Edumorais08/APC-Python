def dinheiros(n, a, b):
   if b<=a and n%2 == 0:
     print(int(n/2*b))
   elif b<a and n%2 == 1:
     print((n//2)*b + a)
   else:
     print(n*a)