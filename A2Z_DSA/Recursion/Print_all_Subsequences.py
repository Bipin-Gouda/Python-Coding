# Question : Print all subsequences

# Method 1 Bit Mnipulation # Method 2 Recursion

nums=[3,1,2,4,5]

def subseq(i,ls):
    if i>=len(nums):
        print(ls)
        return
    ls.append(nums[i])
    subseq(i+1,ls)
    ls.remove(nums[i])
    subseq(i+1,ls)

subseq(0,[])

#%%
   # Question : Print all subsequences with sum=k
    
nums=[3,1,2,4,5]

def subseqk(i,ls,s):
    if i>=len(nums):
        if s==k:
            print(ls)
        return
    ls.append(nums[i])
    s+=nums[i]
    subseqk(i+1,ls,s)
    ls.remove(nums[i])
    s-=nums[i]
    subseqk(i+1,ls,s)
k=5
s=0
subseqk(0,[],s)


#%%


# Print only once

def subseqko(i,ls,s):
    if i>=len(nums):
        if s==k:                    # condition satisfied
            return True
        else:
            return False            # condition not satisfied
    ls.append(nums[i])
    s+=nums[i]
    if(subseqko(i+1,ls,s)==True):
        return True
    ls.remove(nums[i])
    s-=nums[i]
    if(subseqko(i+1,ls,s)==True):
        return True
    return False
k=5
s=0
subseqko(0,[],s)


#%%

# Count the number of subsequences with sum==k

nums=[3,1,2,4,5]
def subseqkc(i,s):
    if i>=len(nums):
        if s==k:                    # condition satisfied
            return 1
        else:
            return 0           # condition not satisfied
    
    s+=nums[i]
    l=subseqkc(i+1,s)
    s-=nums[i]
    r=subseqkc(i+1,s)
       
    return l+r
k=5
s,l,r=0,0,0
print(subseqkc(0,s))


# %%

class Solution:
    def combinationSum(self, candidates, target):                   # NOTE in python ans.append(ls), ans.append(ls[:]) behave differently if ls is a list
        ans=[]                                                      # ans.append(ls) passes a refference of ls so if ls modified it will be modified in ans also
        ls=[]                                                       # ans.append(ls[:]) passes an independent copy of ls
        def func(ind,target):
            if ind>=len(candidates):
                if target==0:
                    print(ls)
                    ans.append(ls[:])               # instead of making ans, ls global we can also pass them 
                    #print(ans)
                return
            #pick the element
            if candidates[ind]<=target:
                ls.append(candidates[ind])
                func(ind,target-candidates[ind])
                ls.pop()

            func(ind+1,target)
 
        func(0,target)
        return ans
      
obj=Solution()
x=obj.combinationSum([2,3,6,7],7)
print(x)