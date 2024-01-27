def longestPalindrome(s):
    # iterate over each charecter
    # for each charecter check if pallindrome or not
    # check for both odd and evenlength substrings
    res=""
    reslen=0
    for i in range(len(s)):
        #odd length
        l,r=i,i
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>reslen:
                res=s[l:r+1]
                reslen=len(res)
            l-=1
            r+=1
        
        #even length
        l,r=i,i+1
        while l>=0 and r<len(s) and s[l]==s[r]:
            if r-l+1>reslen:
                res=s[l:r+1]
                reslen=len(res)
            l-=1
            r+=1
    return res

print(longestPalindrome(input()))