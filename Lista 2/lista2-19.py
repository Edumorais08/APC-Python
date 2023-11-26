def EhBissexto(a):
    if a%4 == 0 and a%100 !=0:
        return 'Bissexto'
    elif a%400 == 0:
        return 'Bissexto'
    else:
        return 'Ano Comum'
    
print(EhBissexto(2023))