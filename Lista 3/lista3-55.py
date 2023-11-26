frase = input()
frase_corrigida = frase

if 'np' in frase:
    frase_corrigida = frase.replace('np', 'mp')
if 'nb' in frase_corrigida:
    frase_corrigida = frase_corrigida.replace('nb', 'mb')

print(frase_corrigida)