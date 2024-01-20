# Method 1 Bit Mnipulation

# Method 2 Recursion

nums=[3,1,2,4,5]

def subseq(i,ls):
    if i>=len(nums):
        print(ls)
        return
    ls.append(nums[i])
    subseq(i+1,ls)
    ls.remove(nums[i])
    subseq(i+1,ls)

#subseq(0,[])


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