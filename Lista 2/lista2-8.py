def formamisteriosa(a,b,c):
    if a==b:
        print('pode ser quadrado')
        if a+b>c and a==b and b==c:
            print('pode ser triangulo equilatero')
        elif a+b>c and a!=b and b!=c:
            print('pode ser triangulo escaleno')
        elif a+b>c:
            print('pode ser triangulo isosceles')

    else:
        print('pode ser retangulo')
        if a+b>c and a==b and b==c:
            print('pode ser triangulo equilatero')
        elif a+b>c and a!=b and a!=c and b!=c:
            print('pode ser triangulo escaleno')
        elif a+b>c and c!=1:
            print('pode ser triangulo isosceles')

formamisteriosa(3,4,5)