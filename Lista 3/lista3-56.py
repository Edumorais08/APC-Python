senha = input()
cond1 = False
cond2 = True
cond3 = True

maiusculas = senha.upper()
minusculas = senha.lower()
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd',
'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
validar1 = 0

#cond1
for i in senha:
    if i.isupper():
        validar1 += 1
        break

for i in senha:
    if i.islower():
        validar1 += 1
        break

for i in senha:
    if i in numeros:
        validar1 += 1
        break

if validar1==3:
    cond1 = True

#cond2
for i in senha:
    if i not in letras and i not in numeros:
        cond2 = False
        break

#cond3
if len(senha)>32 or len(senha)<6:
    cond3 = False

if cond1 and cond2 and cond3:
    print('Senha valida.')
else:
    print('Senha invalida.')