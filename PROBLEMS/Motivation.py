for t in range(int(input())):
    N,X=map(int,input().split())
    Rmax=0
    for i in range(N):
        Si,Ri=map(int,input().split())
        if(Si<=X and Ri>Rmax):
            Rmax=Ri
    print(Rmax)