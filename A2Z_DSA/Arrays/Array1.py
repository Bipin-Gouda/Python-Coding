import array

my_array=array.array('i')
print(my_array)
my_array2=array.array('i',[1,2,3,4,5,6,7])
print(my_array2)

#  Traversing an Array

def Traversearray(arr):
    for i in arr:
        print(i)

Traversearray(my_array2)


#  Accessing array elements

def accessElement(arr,index):
    if index>len(arr)-1:
        print(f"No value in {index}th location")
    else:   
        print(f"The array value is : {arr[index]}")

my_array2[2]=100

accessElement(my_array2,2 )

#  Linear search
def Linearsearch(arr,item):
    item=100
    for i in range(len(arr)):
        if arr[i] == item:
            print(f"element found at location {i}")

Linearsearch(my_array2,100)

         
#  
