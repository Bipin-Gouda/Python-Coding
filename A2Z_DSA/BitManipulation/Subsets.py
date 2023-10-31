# LEETCODE 78
def subsets(nums):
    lst=[]
    for i in range(2**len(nums)):
        temp=[]
        for j in range(len(nums)):
            if i&(1<<j)!=0:
                temp.append(nums[j])
        lst.append(temp)
    return lst

print(subsets([1,2,3]))