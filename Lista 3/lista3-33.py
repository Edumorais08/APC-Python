def maior_norma(v1, v2):
    lista1 = []
    lista2 = []
    for i in v1:
        absoluto = i
        if i<0:
            absoluto = i*(-1)
        lista1.append(absoluto)

    for i in v2:
        absoluto = i
        if i<0:
            absoluto = i*(-1)
        lista2.append(absoluto)

    soma1 = sum(lista1)
    soma2 = sum(lista2)

    if soma1 > soma2:
        print('PRIMEIRO')
    else:
        print('SEGUNDO')
