a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
dragoesmachucados=0
for dragao in range(1,e+1):
    if dragao % a ==0 or dragao % b ==0 or dragao % c ==0 or dragao % d ==0:
         dragoesmachucados+=1
print(dragoesmachucados)