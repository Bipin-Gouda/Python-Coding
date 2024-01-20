# SUM OF 1 to N

# FUNCTIONAL RECURSION
def f(n):
    if n==0:
        return 0
    return n+f(n-1)

print(f(3))      #  f(3)=3+f(2)


# PARAMETERIZED RECURSION
def f(n,s):
    if n==0:
        print(s)
        return
    f(n-1,s+n)

f(3,0)