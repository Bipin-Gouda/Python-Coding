n=int(input())
'''binary=0
while(n>0):
    binary=binary*10+n%2
    n=n//2
binary=int(str(binary).reverse())
print(binary)'''
binary=int(bin(n).replace("0b", ""))
print(type(binary))
#print(int(binary,base=2))
print(~binary)
print(n|0)

