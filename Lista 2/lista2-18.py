def NomeMes(m):
    if m == 1:
        return 'Janeiro'
    elif m == 2:
        return 'Fevereiro'
    elif m == 3:
        return 'Março'
    elif m == 4:
        return 'Abril'
    elif m == 5:
        return 'Maio'
    elif m == 6:
        return 'Junho'
    elif m == 7:
        return 'Julho'
    elif m == 8:
        return 'Agosto'
    elif m == 9:
        return 'Setembro'
    elif m == 10:
        return 'Outubro'
    elif m == 11:
        return 'Novembro'
    elif m == 12:
        return 'Dezembro'
    else:
        return 'Mês inválido'

print(NomeMes(12))