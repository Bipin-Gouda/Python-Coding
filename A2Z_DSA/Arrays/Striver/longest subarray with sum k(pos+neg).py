def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    prefixset={}
    summ=0
    mlen=0
    for R in range(len(nums)):
        summ=summ+nums[R]
        if summ==k:
            mlen=max(mlen,R+1)
        elif summ-k in prefixset:
            mlen=max(mlen,R-prefixset[summ-k])
        if summ not in prefixset: # need to check else if summ existed it will update the index again which will result in not longest subarray
            prefixset[summ]=R             # eg [2,0,0,0,3]   k=3 if no condn op=1 with condn op=3
    return mlen

print()


