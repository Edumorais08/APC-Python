n = int(input())
contador = 0
while n > 0:
    a,b,c = map(int,input().split())
    if a==1 and b==1 or a==1 and c==1 or b==1 and c==1:
        contador += 1
    n -= 1

print(contador)
