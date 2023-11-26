seq1 = input()
seq2 = input()
n = 0
contador = 0

for i in seq1:
    if i != seq2[n]:
        contador += 1
    n += 1

print(contador)