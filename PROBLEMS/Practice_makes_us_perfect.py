# cook your dish here
lst=list(map(int,input().split()))
c=0
for i in lst:
    if i>=10:
        c+=1
print(c)