# Find Position of only set bit , if more set bits exist return -1

def findPosition(N):
    # code here
    count=1
    count2=1
    flag=0
    position=0
    if N==0:
        return -1
    while(N>0):
        if N&1==1:
            count2+=1
            if count2>2:
                return -1
            position=count
        N=N>>1
        count+=1
    if count2>2:
        return -1
    return position

print(findPosition(64))