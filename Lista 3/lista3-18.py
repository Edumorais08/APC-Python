N = int(input())
naluno = 0

while N>0:
    a,b,c = map(int,input().split())
    media = (a+b+c)/3
    if media>= 7:
        print(f'O ALUNO {naluno} FOI APROVADO')
    else:
        print(f'O ALUNO {naluno} FOI REPROVADO')
    naluno += 1
    N -= 1