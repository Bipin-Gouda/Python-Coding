''' Problem Description -: Given an array Arr[ ] of N integers and a positive integer K. The task is to cyclically 
rotate the array clockwise by K.

Note : Keep the first position of the array unaltered.
Example 1:

5 = Value of N
{10, 20, 30, 40, 50}  —Elements of Arr[ ]
2 = Value of K
Output: 10 40 50 20 30
'''

N=int(input())
lst=[]
for i in range(N):
    lst.append(input())    # given input in next line for array not direct ( Take Care)
k=int(input())
for i in range(k):
    temp=lst.pop()
    lst.insert(1,temp)
print(" ".join(lst))