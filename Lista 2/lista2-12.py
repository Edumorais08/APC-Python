def jogadas(a,b):
    ma = max(a,b)
    me = min(a,b)
    d = ma-me

    if a == b:
        print('0')
    elif d%10 == 0:
        print(d//10)
    else:
        print((d//10)+1)