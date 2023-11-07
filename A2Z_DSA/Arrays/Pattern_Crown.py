def numberCrown(n: int) -> None:
    # Write your solution here.
    temp=n*2-2
    for i in range(1,n+1):
        x=0
        for j in range(1,i+1):
            x+=1
            print(x,end='')
            
        print(' '*temp,end='')
        
        while(x>0):
            print(x,end='')
            x-=1
        temp-=2
        print()


numberCrown(5)




#%%%
def numberCrown(n: int) -> None:
    # Write your solution here.
    temp=0
    for i in range(n,0,-1):
        x=n
        for j in range(i,0,-1):
            x-=1
            print('* ',end='')
            
        print('  '*temp,end='')
        
        while(x<n):
            print('* ',end='')
            x+=1
        temp+=2
        print()


numberCrown(3)

def numberCrown(n: int) -> None:
    # Write your solution here.
    temp=n*2-2
    for i in range(1,n+1):
        x=0
        for j in range(1,i+1):
            x+=1
            print('* ',end='')
            
        print('  '*temp,end='')
        
        while(x>0):
            print('* ',end='')
            x-=1
        temp-=2
        print()


numberCrown(3)


#%%
def numberCrown(n: int) -> None:
    # Write your solution here.
    temp=n*2-2
    for i in range(1,n+1):
        x=0
        for j in range(1,i+1):
            x+=1
            print('* ',end='')
            
        print('  '*temp,end='')
        
        while(x>0):
            print('* ',end='')
            x-=1
        temp-=2
        print()


numberCrown(3)

def numberCrown(n: int) -> None:
    # Write your solution here.
    temp=2
    for i in range(n-1,0,-1):
        x=n
        for j in range(i,0,-1):
            x-=1
            print('* ',end='')
            
        print('  '*temp,end='')
        
        while(x<n):
            print('* ',end='')
            x+=1
        temp+=2
        print()


numberCrown(3)





# %%
