# Note how end case has been handled

def summaryRanges(nums):
    ans=[]
    if not nums:
        return ans
    start=nums[0]
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]+1:
            if start==nums[i-1]:
                ans.append(f"{nums[i-1]}")  
            else:
                ans.append(f"{start}->{nums[i-1]}")
            start=nums[i]
    if start == nums[-1]:
        ans.append(f"{start}")
    else:
        ans.append(f"{start}->{nums[-1]}")
    return ans  

print(summaryRanges([1,2,4,5,7]))
    
