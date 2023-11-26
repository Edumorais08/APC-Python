#p=peso, s=sexo e a=altura
def ComoVaiSuaSaude(p, s, a):
    PI =  (72.7 * a) - 58
    if s == 'F':
      PI = (62.1 * a) - 44.7
    IMC = p / (a * a)
    diferenca_peso_PI = abs(p - PI)
    diferenca_percentual = (diferenca_peso_PI / PI) * 100

    if diferenca_percentual <= 5 and IMC >= 18.5 and IMC < 25:
        return 'Você tem uma saúde ótima!'
    elif diferenca_percentual <= 10 and IMC >= 18.5 and IMC < 25:
        return 'Você tem uma saúde boa.'
    elif p < PI and IMC < 18.5:
        return 'Atenção: Fique atento ao baixo peso!'
    elif diferenca_percentual > 10 and IMC >= 25 and IMC < 30:
        return 'Cuidado: Medidas acima do padrão!'
    elif diferenca_percentual > 10 and IMC >= 30:
        return 'Procure Ajuda: Excesso de medidas!'
    else:
        return 'Sem apontamento.'

print(ComoVaiSuaSaude(50,'M',1.70))