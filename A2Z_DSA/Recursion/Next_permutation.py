def nextPermutation(nums):
        """
        Do not return anything, modify nums in-place instead.  # Brute Force
        """
        ans=[]
        def func(ind):
            if ind==len(nums):
                ans.append(nums[:])
                return 
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                func(ind+1)
                nums[ind],nums[i]=nums[i],nums[ind]

        func(0)
        #print(ans)
        for i in range(0,len(ans)):
            if ans[i]==nums and i!=len(ans)-1:
                nums=ans[i+1]
                return nums
            elif ans[i]==nums and i==len(ans)-1:
                nums=ans[0]
                return nums
        
            
nextp=nextPermutation([1,2,3])
print(nextp)