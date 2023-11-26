n = int(input())
c = 1
while n > 0:
    if c%3==0 and c%5==0:
        print('Fizz Buzz')
    elif c%3==0:
        print('Fizz')
    elif c%5==0:
        print('Buzz')
    else:
        print(c)
    c += 1
    n -= 1