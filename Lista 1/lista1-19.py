#para tirar aspas ' '. join
du,dudu,edu = map(float,input().split())
conta = ('{:.2f}'.format(du*1.1),'{:.2f}'.format(dudu*1.1),'{:.2f}'.format(edu*1.1))
print(' '.join(conta))
total = (du + dudu + edu)*1.1
print('{:.2f}'.format(total))