import numpy as np

twoDArray=np.array([[11,12,13,14],[1,2,3,4],[15,16,17,18],[6,7,8,9]])
print(twoDArray,'\n')
new2Darray=np.insert(twoDArray,0,[0,0,0,0],axis=0)
print(new2Darray,'\n')
new2Darray=np.append(new2Darray,[[1,1,1,1]],axis=0)
print(new2Darray)

# Access elements in 2D array
def AccessElements(array,r_index,c_index):
    #len(array) no of rows , len(array[0]) no of columns
    if r_index>=len(array) or c_index>=len(array[0]):
        print('Out of bounds')
    else:
        print(array[r_index][c_index])

AccessElements(new2Darray,2,3)
