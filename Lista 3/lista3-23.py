n = int(input())
habilidades = list(map(int,input().strip().split()))[:n]

habilidades.sort(reverse=True)
titulares = habilidades[:11]
reservas = habilidades[11:22]

somatitu = sum(titulares)
somares = sum(reservas)

dif = somatitu - somares
print(dif)
