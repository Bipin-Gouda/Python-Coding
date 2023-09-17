for t in range (int(input())):
    n,a,b,c=map(int,input().split())           
    if n<=(a+c) and n<=b:    
        print('YES')
    else:
        print('NO')
        
# n must be less than b(vegetables),a+c is the max possible val if b>a+c