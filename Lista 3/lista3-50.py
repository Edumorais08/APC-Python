palavra = input()
contador_de_minusculas = 0
contador_de_maiusculas = 0

for i in palavra:
    if i.isupper():
        contador_de_maiusculas += 1
    else:
        contador_de_minusculas += 1

if contador_de_maiusculas > contador_de_minusculas:
    print(palavra.upper())
else:
    print(palavra.lower())