n = int(input())

while n>0:
    palavra = input()
    tam = len(palavra)
    num = str(tam - 2)
    ult = tam -1
    if tam>10:
        print(f'{palavra[0]}{num}{palavra[ult]}')
    else:
        print(palavra)
    n -= 1