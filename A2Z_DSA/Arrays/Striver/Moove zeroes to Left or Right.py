#ie moove non zeroes to left so if 0 do nothing else swap  
def moveZerosright(n,a):
    l=0
    for r in range(n):
        if a[r]:
            a[l],a[r]=a[r],a[l]
            l+=1
    return a

# if moove zeroes to left if 0 found swap it  # order gets changed here
def moveZerosleft(n,a):
    l=0
    for r in range(n):
        if a[r]==0:
            a[l],a[r]=a[r],a[l]
            l+=1
    return a

x=moveZerosright(7,[1,0,2,4,3,0,1])
y=moveZerosleft(7,[1,0,2,4,3,0,1])
print(x)
print(y)
