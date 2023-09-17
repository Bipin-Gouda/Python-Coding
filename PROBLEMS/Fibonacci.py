# FIbo series 0  1  1  2  3  5  8 .....
          #   n1 n2 n3

N=int(input())
n1=0
n2=1
print(n1,"",n2,end=" ")
for i in range(N):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")
