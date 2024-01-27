def isAnagram(s,t):
    if len(s)!=len(t):
        return False
    di1={}
    di2={}
    for i in s:
        di1[i]=di1.get(i,0)+1
    for j in t:
        di2[j]=di2.get(j,0)+1
    if di1==di2:
        return True
    return False
s,t=input().split()
print(isAnagram(s,t))