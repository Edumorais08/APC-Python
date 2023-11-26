N = int(input())
M = int(input())
album =[]
Z = N
figu=[]

while M>0:
    x = int(input())
    album.append(x)
    M -= 1

for ele in album:
    if ele not in figu:
        figu.append(ele)

print(Z - len(figu))
