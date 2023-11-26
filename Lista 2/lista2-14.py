def qtdcopos(n):
    if n%4 != 0:
        x = 4 - (n%4)
        print('Pode voltar pro ceubinho, deivis! Falta(m)', x, 'copo(s)! ')
    elif n == 0:
        print('Pode voltar pro ceubinho, deivis! Falta(m) 4 copo(s)! ')
    else:
        print('Pode levar pros calourinhos, deivis!')