def pacotesDeBolacha(m,n,k):
  print(m - n * k)

m,n,k = map(int,input().split())
pacotesDeBolacha(m,n,k)

#----------------------------------------

def pacotesDeBolacha(m,n,k):
    teste = m-n
    bpa = n*k
    mb = m - bpa
    if teste<=0:
        print(teste)
    if mb < n and teste>0:
        print(mb)