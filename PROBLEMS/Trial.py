lst=[10, 20, 30, 40, 50]
lst.sort(reverse=True)
print(lst)
x=sorted(lst,reverse=True)
print(x)
lst=x
print(lst)
x=sorted(lst,key=2)
print(x)