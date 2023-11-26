palavra = input()
letras = list(palavra)
vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u', 'Y', 'y']
c = 0
palavra_com_pontos = []

for i in letras:
    if i not in vogais:
        palavra_com_pontos.append('.')
        if i.isupper():
            minuscula = i.lower()
            palavra_com_pontos.append(minuscula)
        else:
            palavra_com_pontos.append(i)

print(''.join(palavra_com_pontos))