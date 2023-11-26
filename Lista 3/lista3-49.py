n = int(input())
genoma = input()

def decodificar(genoma, nec):

    ## ordem dos nucleotídeos = AGCT
    nucleot = [0,0,0,0]
    interrog = 0

    for letra in genoma:
        if letra == 'A':
           nucleot[0]+=1
        elif letra == 'G':
           nucleot[1]+=1
        elif letra == 'C':
           nucleot[2]+=1
        elif letra == 'T':
           nucleot[3]+=1
        else:
            interrog+=1

    necessario = 0

    for i in nucleot:
        if i>nec:
            return 'Feiticeiro misterioso'
        else:
            dif = int(nec-i)
            if dif == 0:
                necessario +=0
            else:
                necessario+=dif

    if necessario == 0 or necessario%interrog == 0:
        return 'Segredos desvendados'
    else:
        return 'Feiticeiro misterioso'

if n%4 == 0:
    nec = n/4
    print(decodificar(genoma,nec))
else:
    print('Feiticeiro misterioso')