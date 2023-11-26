def Alfabeto(x):
    codigo = ord(x)
    if codigo==97 or codigo==101 or codigo==105 or codigo==111 or codigo==117 or codigo==65 or codigo==69 or codigo==73 or codigo==79 or codigo==85:
         return 'Vogal'
    else:
         return 'Consoante'
    

print(Alfabeto('a'))