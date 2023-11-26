PA,PB,T1,T2 = map(float,input().split())
porcentagem1 = T1/100 +1
porcentagem2 = T2 / 100 +1

crescimento_a = int(PA)
crescimento_b = int(PB)
contador = 0

while crescimento_a < crescimento_b:
    if contador > 23500 and crescimento_a < crescimento_b:
        print("A nunca alcancara B.")
        break
    crescimento_a = int(crescimento_a * porcentagem1)
    crescimento_b = int(crescimento_b * porcentagem2 )
    contador += 1

if contador > 1000 and contador <23500:
    print('Mais de um milenio.')
elif contador < 1000:
    print(f'Vai alcancar em {contador} ano(s).')


