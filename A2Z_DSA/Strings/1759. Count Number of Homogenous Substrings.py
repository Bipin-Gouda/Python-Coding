'''Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.
A string is homogenous if all the characters of the string are the same. A substring is a contiguous sequence of characters within a string.
Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.'''

class Solution:
    def countHomogenous(self, s: str) -> int:
        res=0 # sum
        count=1
        prev=s[0]
        for i in range(1,len(s)):
            if s[i]==prev:
                count+=1
            else:
                if count!=1:
                    res=res+count*(count+1)/2
                elif count==1:
                    res+=1
                count=1
            prev=s[i]     #as the last aa is s[i]==prev till the end so it doesnt go to else block ro calc its count
        res+=count*(count+1)/2
        res=res%(10**9+7)
        return round(res)
    
obj=Solution()
print(obj.countHomogenous(input()))
#abbccca