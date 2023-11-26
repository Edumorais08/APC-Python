#if sem==0 :
def qualPeriodo(m,a,s):
    ano = int(str(m)[:4])
    sem = int(str(ano)[-1:])
    ano_ingresso = int(str(m)[:2])
    ano_atual = int(str(a)[-2:])
    semestre = ((ano_atual - ano_ingresso)*2)+s
    if sem==0 :
     print(semestre + 1)
    else:
     print(semestre)
    