n1,n2,n3 = map(float,input().split())
p1,p2,p3 = map(int,input().split())

resultado=(n1*p1 + n2*p2 + n3*p3)/(p1+p2+p3)
print("{:.6f}".format(resultado))
