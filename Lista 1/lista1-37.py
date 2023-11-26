def print_rectangle(a,b,c):
  print(a)
  print(a * '+')
  print('+'+' '*(a-2)+'+')
  print(a * '+')
  print(b)
  print(b * '+')
  print('+'+' '*(b-2)+'+')
  print(b * '+')
  print(c)
  print(c * '+')
  print('+'+' '*(c-2)+'+')
  print(c * '+')


a,b,c = map(int,input().split())
print_rectangle(a,b,c)
