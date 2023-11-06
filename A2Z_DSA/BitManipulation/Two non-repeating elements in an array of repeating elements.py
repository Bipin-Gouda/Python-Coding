# Find the two non-repeating elements in an array of repeating elements

class Solution:
    def singleNumber(self, nums):
        res=0
        for i in nums:
            res=res^i
        mask=res&~(res-1)
        temp=res
        for i in nums:
            if (i & mask)>0:
                temp=temp^i
        val1=temp
        val2=val1^res
        lst=[val1,val2]
        
        return sorted(lst)
                

obj=Solution()
print(obj.singleNumber([1,2,3,2,1,4]))

