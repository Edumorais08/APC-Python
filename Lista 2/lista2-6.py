def dominos(N,M):
    dim = N*M
    if dim%2 == 0:
        print(int(dim/2))
    else:
        print(dim//2)