n = int(input())
vet1 = list(map(int,input().strip().split()))[:n]
vet2 = list(map(int,input().strip().split()))[:n]
i = 0
verify = []

while n>0:
    xu = vet1[i]
    xv = vet2[i]
    x = xu * xv
    verify.append(x)
    n -= 1
    i += 1


soma = sum(verify)
if soma == 0:
    print('ortogonais')
else:
    print(soma)
