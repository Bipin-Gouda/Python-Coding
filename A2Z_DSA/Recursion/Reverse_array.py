# Reverse with using a single variable, Functional code


a=[1,2,3,4,5,9]
n=len(a)
def rev(l):
    if l>=n/2:
        return 
    a[l],a[n-l-1]=a[n-l-1],a[l]
    rev(l+1)

rev(0)
print(a)