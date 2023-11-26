def quantosJantam(n,g,f,c):
    if g<=f and g+c<=n:
        print(g+c)
    elif f<g and f+c<=n:
        print(f+c)
    elif g+c>n and f+c>n:
        print(n)
