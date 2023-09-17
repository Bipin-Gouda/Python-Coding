# Reversing an array     

arr=list(map(int,input("Enter a number: ").split()))
print(arr[::-1])
end=len(arr)-1
i=0
while i<end:
    arr[i],arr[end]=arr[end],arr[i]
    i+=1
    end-=1   
print(arr)
