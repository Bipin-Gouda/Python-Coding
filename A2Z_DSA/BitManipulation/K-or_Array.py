# LEETCODE K-or Array 
'''
You are given a 0-indexed integer array nums, and an integer k.

The K-or of nums is a non-negative integer that satisfies the following:

The ith bit is set in the K-or if and only if there are at least k elements of nums in which bit i is set.
Return the K-or of nums.

Note that a bit i is set in x if (2i AND x) == 2i, where AND is the bitwise AND operator.
'''
nums = [7,12,9,8,9,15]
nums=[2,12,1,11,4,5]
nums=[10,8,5,9,11,6,8]
k = 1

nu=0
for i in range(31,-1,-1):
    
    count=0
    for j in range(len(nums)):
        if nums[j]&(1<<i):
            count+=1
    
    if count>=k:
        
        nu=nu|(1<<(i))
   
print(nu)