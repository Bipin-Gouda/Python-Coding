class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n=len(word)
        for i in range(1,(n//k)+1):
            m=i*k
            for j in range(m,n):
                if word[j-m]!=word[j]:   #can use all()
                    break
                if j==n-1:
                    return i
        if n%k!=0:
            return n//k+1
        return n//k
    
obj=Solution()
print(obj.minimumTimeToInitialState(input(),int(input())))


# if all(word[j-m]==word[j] for j in range(m,n)):
#       return i