# Check Palindrome and armstrong

num=int(input("Enter a number:"))
temp=num
rev=0
while(temp):
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10       # integer divisn else rev = inf  (infinity in python)
print(rev)
if(num==rev):
    print("%d is a palindrome"%num)    
else:
    print("%d is not a palindrome"%num)
temp2=num
lst=[]
dig_count=0
while(temp2):
    rem=temp2%10
    lst.append(rem)
    dig_count+=1
    temp2=temp2//10    # integer divisn used else float ho jayega fir dikkat
print("Number of digits:",dig_count)
print("Reversed number:",lst)                  # int join ni hoga string join hota h
arm=sum(list(map(lambda x:x**dig_count,lst)))
print("It is Armstrong:",num==arm)