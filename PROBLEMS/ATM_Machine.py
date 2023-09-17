for t in range(int(input())):
    N,K=map(int,input().split())
    lst=list(map(int,input().split()))
    for n in lst:
        if n<=K:
            print(1,end='')
            K=K-n
        else:
            print(0,end='')
    print()