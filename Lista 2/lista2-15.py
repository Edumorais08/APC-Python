def piscininha(x,y,w,h,a,b):
    pax = x
    pbx = x+w
    pay = y
    pby = y+h

    if a>pax and a<pbx and b>pay and b<pby:
        print('Dando um tchibum')
    elif a<pax or a>pbx or b<pay or b>pby:
        print('Tomando um solzin')
    else:
        print('So com os pezin dentro da agua')