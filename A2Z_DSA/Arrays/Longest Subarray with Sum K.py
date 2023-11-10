'''Problem Statement
You are given an array 'a' of size 'n' and an integer 'k'. Find the length of the longest subarray of 'a' whose sum is equal to 'k'.
Example :
Input: ‘n’ = 7 ‘k’ = 3
‘a’ = [1, 2, 3, 1, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = ‘3’ are:
[1, 2], [3], [1, 1, 1] and [1, 1, 1]
Here, the length of the longest subarray is 3, which is our
final answer.
'''
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    # using 2 pointer approach
    nums=a
    left = 0
    res= 0
    max_length = 0
    
    for right in range(len(nums)):
        res += nums[right]
        
        # Check if current_sum equals K, we use while bc we need to remove the elements till which result is greater than k (do dry run)
        while res > k:
            res -= nums[left]
            left += 1
        
        # Update max_length
        if res == k:
            max_length = max(max_length, right - left + 1)
    
    return max_length
