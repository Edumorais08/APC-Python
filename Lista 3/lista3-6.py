n = int(input())
contador = 1
while n > 0:
    if contador == 1:
        print(f'{contador} elefante incomoda muita gente...' )
    else:
         print(f'{contador} elefantes incomodam muita gente...' )
    contador += 1
    c = contador-1
    n_incomodam = ' incomodam,'*c + ' incomodam'
    print(f'{contador} elefantes{n_incomodam} muito mais...' )
    n -= 1