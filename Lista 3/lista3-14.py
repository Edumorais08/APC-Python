n = int(input())
h = n - 1

while h > 1:
    if n % h == 0:
        break
    h -= 1

if h == 1:
    print('primo')
elif n==1:
    print('regular')
else:
    print('regular')