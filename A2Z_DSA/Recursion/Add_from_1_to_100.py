def addn(n):
    if n==1:                    # base condition
        return 1
    return n+addn(n-1)          # actual code

print(addn(100))


