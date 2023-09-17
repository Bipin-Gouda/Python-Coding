for t in range(int(input())):
    lst=map(int,input().split())
    lst=list(lst)
    if all(item in lst[:2] for item in lst[2:4]):
        print(1)
    elif all(item in lst[:2] for item in lst[4:]):
        print(2)
    else:
        print(0)
        
        
# all() method  used to compare all elements in a sequence
# any() method  used to find any one comparison