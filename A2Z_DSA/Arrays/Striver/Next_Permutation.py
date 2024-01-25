def nextPermutation(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    ind=-1
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[i+1]:
            ind=i
            break
    if ind==-1:
        nums.reverse()
    else:
        for i in range(len(nums)-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break

        nums[ind+1:] = reversed(nums[ind+1:])


#%%
def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=nums
        ans=[]
        def func(ind):
            if ind==len(nums):
                ans.append(nums.copy())
                return 
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                func(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]

        func(0)
        for i in range(0,len(ans)):
            if ans[i]==nums and i!=len(ans):
                return ans[i+1]
            elif ans[i]==nums and i==len(ans):
                return ans[0]
                