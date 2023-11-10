class Solution:
    def countHomogenous(self, s: str) -> int:
        res=0 # sum
        count=1
        prev=s[0]
        ls=[]
        for i in range(1,len(s)):
            if s[i]==prev and i<len(s):
                count+=1
            else:
                ls.append(count)
                if count!=1:
                    res=res+count*(count+1)/2
                elif count==1:
                    res+=1
                count=1
            prev=s[i]
        ls.append(count)     #as the last aa is s[i]==prev till the end so it doesnt go to else block ro calc its count
        res+=count*(count+1)/2
        return round(res),ls
            
obj1=Solution()
print(obj1.countHomogenous('aaaaaaa'))