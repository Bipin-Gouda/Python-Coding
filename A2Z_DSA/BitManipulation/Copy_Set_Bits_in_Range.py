"""
Given two numbers X and Y, and a range [L, R] where 1 <= L <= R <= 32.
You have to copy the set bits of 'Y' in the range L to R in 'X'. Return this modified X.
Note: Range count will be from Right to Left & start from 1
"""
def setSetBit(x, y, l, r):
    # code here
    mask=0
    for i in range(l-1,r):  # to reach 4 we need 3 shifts
        mask=mask|(1<<i)
    y=y&mask
    res=x|y
    return res

print(setSetBit(44, 3, 1, 5))