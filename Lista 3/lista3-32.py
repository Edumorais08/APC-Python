def remove_duplicatas(lista):
    novalista = []
    x = 0
    for i in lista:
        if i not in novalista:
            novalista.append(i)

    return(novalista)