from array import * 
# else we need to do array.array( )  array method of array class Class.method()

# 1. Create an array and traverse
arr1=array('i',[1,2,3,4,5,6])

for i in arr1:
    print(i , end=" ")
print()

# 2. Access individual elements through indexes
for i in range(len(arr1)):
    print(arr1[i], end=" ")
print()

# 3. Append any value to the array using append() method
arr1.append(25)
print(arr1)

# 4. Insert value in array using insert() method
arr1.insert(2,30)
print(arr1)

# 5. Extend python array using extend() method
arr2=array('i',[11,12,13,1,2,3,30])
arr1.extend(arr2)
print(arr1)
print(arr2)

# 6. Add items from list using fromlist() method
templist=[20,21,22]
arr1.fromlist(templist)
print(arr1)

# 7. Remove any array element using remove() method
arr1.remove(30)
print(arr1)

# 8. Remove last array element using pop() method
removed_ele=arr1.pop()
print(removed_ele)
print(arr1)

# 9. Fetch any element index through index() method using value
print(arr1.index(21))

# 10. Reverse a python array using reverse() method
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method
print(arr1.buffer_info())

# 12. Check for number of occurences  of an element using count() method
print(arr1.count(3))

'''# Counter gives dictionary, counts all
from collections import Counter
x=Counter(arr1)
print(x)'''

# 13. Convert array to string using tobytes() method
strTemp=arr1.tobytes()
print(strTemp)
ints=array('i')
ints.frombytes(strTemp)
print(ints)

# 14. Convert array to python list using tolist() method
lst=arr1.tolist()
print(lst)

# 15. Append a string to char array using fromstring() method


# 16. Slice elements from array
print(arr1[3:7])
print(arr1[0])
print(arr1[-1])
print(arr1[:])
print(arr1[-7:-1])   #-1 to -7 not working
print(arr1[::-1])

 