def printer(N,cnt): 
    if cnt==N:
        return
    
    cnt+=1
    print("Name",cnt)
    printer(N,cnt)
    


printer(3,0)

'''
def main():
    #N=int(input())
    #printer(N,0)
    print("Hello World!")

if __name__ == "__main__":
    main()
    '''