# Function to check if given number n is a power of two.

def isPowerofTwo(n):
    ##Your code here
    count=0
    if n==0:
        return False
    while(n>0):              # There should be only one '1' in binary to be of power 2 
        if n&1==1:
            count+=1
            if count>1:
                return False
        n=n>>1
    
    return True

print(isPowerofTwo(64))