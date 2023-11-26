def classificador(a,b,c):
    maior = max(a,b,c)
    valores = [a,b,c]
    sorteados = sorted(valores)
    menor1 = sorteados[0]
    menor2 = sorteados[1]
    if a+b>c and b+c>a and a+c>b:
        print('triangulo')
        if a!=b and a!=c and b!=c:
            print('escaleno')
        if a==b or b==c or a==c:
            print('isosceles')
        if a==b and b==c:
            print('equilatero')
        if (maior)**2 == (menor1)**2 + (menor2)**2:
            print('retangulo')
    else:
        print('gondim sendo gondim')

classificador(3,4,5)