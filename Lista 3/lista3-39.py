n = int(input())
x=0

while n>0:
    conta = input()
    if conta=='++X' or conta=='X++':
        x += 1
    else:
        x -= 1
    n -= 1

print(x)