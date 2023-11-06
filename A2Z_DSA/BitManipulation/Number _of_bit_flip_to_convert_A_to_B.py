# Find number of bits needed to be flipped to convert A to B

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        #only countdiff bits first ,xor = if diff => 1
        a=a^b
        # now count 1s ie set bits
        count=0
        while(a>0):
            a=a&(a-1)
            count+=1
        return count
    
obj=Solution()
print(obj.countBitsFlip(12,7))