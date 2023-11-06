# Every number appears k times except one (k=3 here)

def singleNumber(nums):
        B = [0] * 32
        for x in nums:
            # Ensure negative numbers are handled correctly
            if x < 0:
                x = 2**32 + x  # Convert negative number to its 32-bit representation 2s complement
            for i in range(32):     # 2**32 +(-7) so becomes less than 2**32 and we get the 2s complement
                if x & (1 << i):    # wrt 32 bits 
                    B[i] += 1
        ans = 0
        for i in range(32):
            if B[i] % 3 != 0:
                ans =ans| (1 << i)
        # Handle negative result
        if ans > 2**31 - 1:   # ie answer beyond range 
            ans = ans-2**32
        return ans

print(singleNumber([1,3,3,3,4,4,4,1,1,5,5,5,8,6,6,7,7,7,6]))