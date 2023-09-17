# Reverse an array using recursion
arr=[1,2,3,4,5,6]
i=0
n=len(arr)-1

def reversal(arr,i,n):
    if i>=n:
        return 
    arr[i],arr[n]=arr[n],arr[i]
    i+=1
    n-=1
    #print(arr)
    reversal(arr,i,n)

reversal(arr,i,n)
print(arr)