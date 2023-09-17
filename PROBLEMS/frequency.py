lst=list(map(int,input().split()))
d={}
for i,n in enumerate(lst):
    if n in d:
        d[n]+=1
    else:
        d[n]=1
print(d)

#%%
from collections import Counter
count=Counter(map(int,input().split()))
print(count)