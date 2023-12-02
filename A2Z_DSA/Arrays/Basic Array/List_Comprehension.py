# Basic list Comprehension

lst=[x*2 for x in range(1,5)]
print(lst)
print(sum([x*2 for x in range(1,5)]))
print(max([x*2 for x in range(1,5)]))
print([m/5 for m in lst])

# Conditional list comprehension

prev_list=[-1,10,-20,2,-90,60,45,20]
new_list=[number for number in prev_list if number>0]
print(new_list)

print([number**2 for number in prev_list if number>0 ]) 

print([number if number>0 else 'negative number' for number in prev_list]) 

# Checking for consonants only using function and list comprehension

sentence='My name is Bipin'
def is_consonant(letter):
    vowels='aeiou'
    return letter.isalpha() and letter.lower() not in vowels

print(is_consonant('i'))
print(is_consonant('n'))

consonants=[i for i in sentence if is_consonant]
print(consonants)


# using functions

prev_list=[-1,10,-20,2,-90,60,45,20]
print([number if number>0 else 'negative number' for number in prev_list]) 

# OR

def get_number(number):
    return number if number>0 else 'negative number'

print([get_number(number) for number in prev_list]) 
