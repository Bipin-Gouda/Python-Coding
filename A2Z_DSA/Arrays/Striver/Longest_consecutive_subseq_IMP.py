class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)

        maxlen=0
        
        for i in nums:
            #check start of array
            if i-1 not in numset:
                length=0
                while i+length in numset:
                    length+=1
                maxlen=max(maxlen,length)
        return maxlen







#%%




class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        # Note the pattern by default length is 1
        c = 1
        maxm = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    c += 1
                else:
                    maxm = max(maxm, c)
                    c = 1

        return max(maxm, c)