N=int(input())
lst=[]
for i in range(N):
    lst.append(int(input()))
M=int(input())
lst2=[]
for i in range(M):
    lst2.append(int(input()))
sum1=sum(lst)
sum2=sum(lst2)
c1=0
c2=0
if(sum1%2==0 and sum2%2==0):
    print(0)
else:
    for i in lst:
        if i%2!=0:
            c1+=1
        else:
            c2+=1
    if(c1%2!=0):
        for i in lst():
            if i%2==0:
                temp1=i
                lst.remove(i)
                break
    if(c2%2!=0):
        for i in lst2():
            if i%2==0:
                temp2=i
                lst.remove(i)
                break
    
    