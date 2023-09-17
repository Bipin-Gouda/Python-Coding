"""Question
   Given two non negative integers n1 and n2 where n1<n2. The task is to find the total no of integers in the range
   interval [n1,n2] (both inclusive) which have no repeated digits.
   
   Example: n1=11  ,  n2=15  11 has repeated digits but 12,13,14,15 don't therefore count=4 """


from collections import Counter
int1=int(input())
int2=int(input())
temp1=str(int1)
temp2=str(int2)
c=0
for i in range(int1,int2+1):
    temp3=str(i)
    di=Counter(temp3)
    lst=di.values()
    x=0
    for i in lst:
        if(i>1):
            x=1
    if (x==0):
        c+=1
print(c)