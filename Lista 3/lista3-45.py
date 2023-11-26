frase = input()
nova_frase = ""

for i in range(len(frase)):
    if frase[i] == " ":
        nova_frase += " "
    elif i > 0 and frase[i-1] != " ":
        nova_frase += " " + frase[i]
    else:
        nova_frase += frase[i]

print(nova_frase)