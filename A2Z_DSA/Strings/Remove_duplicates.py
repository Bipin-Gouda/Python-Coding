# Remove Duplicates from String

def removeDuplicates(str):
    # code here
    hashset=set()
    ans=""
    for ch in str:
        if ch not in hashset:
            hashset.add(ch)
            ans+=ch
    return ans

print(removeDuplicates(input()))