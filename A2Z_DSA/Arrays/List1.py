# Creation, Traversal, Updation
import numpy as np

shoppinglist=['Milk','Bread','Butter']
print(shoppinglist)

for i in range(len(shoppinglist)):
    shoppinglist[i]=shoppinglist[i]+'-1'
print(shoppinglist)

empty=[]
for i in empty:
    print("I am empty")

# Slicing
newlst=[1,2,3,4,5,6,7,8,9,0]
print(newlst[0])
print(newlst[:])
print(newlst[::-1]) # reversal

newlst[0:2]=['a','b']
print(newlst)

temp1=np.random.rand(3,3)
# print(temp1)

# split() , join()
a='spam'
b=list(a)
print(b)
c='spam spam spam'
d=list(c)
print(d)
e=c.split()
print(e)
e=('-').join(e)
print(e)




    