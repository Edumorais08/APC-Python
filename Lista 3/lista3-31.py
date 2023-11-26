Bill = int(input())
caixa = list(map(int,input().split()))
chinelos = sorted(caixa)
tam = len(chinelos)
i = 0

while tam>0:
    x = chinelos[i]
    if x>=Bill:
        print(i)
        break
    i += 1
    tam -= 1

if x<Bill:
    print(-1)