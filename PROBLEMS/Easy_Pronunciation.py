'''
vow=['a','e','i','o','u']
for t in range(int(input())):
    count=0
    flag=0
    strlen=int(input())
    strx=input()
    for m in strx:
        if count>=4:         # if not done flag=1 NO k bad fir YES print ho jayega
            print('NO')
            flag=1
            break          # problem in break part NOTsuccess
        if m not in vow :
            count+=1
        else:
            count=0
    if(flag==0):
        print('YES')
 '''
        
'''
vowels=['a','e','i','o','u']
for t in range(int(input())):     #success
    n=int(input())
    st=input()
    c=0
    flag=0
    for i in st:
        if i in vowels:
            c=0
        else:
            c+=1
        if c>=4:
            flag=1
    if flag:
        print("NO")
    else:
        print("YES") 
        
            
vowels=['a','e','i','o','u']
for t in range(int(input())):
    n=int(input())
    st=input()
    c=0
    flag=0
    for i in st:                           #success
        if i in vowels:
            c=0
        else:
            c+=1
        if c>=4:
            flag=1
    if (flag==1):
        print("NO")
    else:
        print("YES") '''


vow=['a','e','i','o','u']
for t in range(int(input())):
    n=int(input())
    st=input()
    c=0
    flag=0                               #success
    for i in st:
        if i not in vow:
            c+=1
        else:
            c=0
        if c>=4:
            flag=1
    if (flag==1):
        print("NO")
    else:
        print("YES") 