# Average Temperature
days=int(input("How many day's temperature: "))
lst=[int(input(f"Day {i+1}'s high temp :")) for i in range(days)]
avgtemp=sum(lst)/len(lst)
print("avgtemp is :",avgtemp)
count=0
for i in range(len(lst)) :
    if lst[i]>avgtemp: count+=1
print(f"{count} day(s) above average")