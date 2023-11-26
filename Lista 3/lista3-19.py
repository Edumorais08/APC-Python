a=list(map(int,input().strip().split()))
n=len(a)

contador=0

for x in range (n):
  for y in range (x+1 , n):
    if a[x] > a[y]:
     contador+=1
print(contador)