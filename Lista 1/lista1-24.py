def age(days):
    anos = days // 360
    meses = (days % 360) // 30
    dias = (days % 360) % 30
    print(f"{anos} ano(s), {meses} mes(es) e {dias} dia(s)")

a,b,c = map(int,input().split())
age(a)
age(b)
age(c)