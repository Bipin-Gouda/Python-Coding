# Default values
'''Now sometimes when you are creating our attributes, we might want to set a default value to start with.
And if at some point later in our program we want to modify it, we can do it at that point.'''

#setting default values

class YouTube:
    def __init__(self, username, subscribers=0,subscriptions=0):  # if subscribers not passed as parameter, by default zero subscribers
        self.username=username
        self.subscribers=subscribers
        self.subscriptions=subscriptions

    def subscribe(self,user):   #user is another object ie we can also pass another object to a method
        user.subscribers+=1
        self.subscriptions+=1
        

# the no of subscribers initially will be zero so it doesnt make sense pass zero everytime we create an object (user) so default val to 0

user1=YouTube("Bipin")
user2=YouTube("Renad")
#user2.subscribers=5    # changing the values

user1.subscribe(user2)

print(user1.username)
print(f"subscribers of {user1.username}: {user1.subscribers}")
print(f"subscriptions of {user1.username}: {user1.subscriptions}")


print(user2.username)
print(f"subscribers of {user2.username}: {user2.subscribers}")
print(f"subscriptions of {user2.username}: {user2.subscriptions}")

# Now it's very advisable to use all attributes inside init function, because if you mistype them, python will take it as a new parameter
# example
print()
user2.subscriber=10   # new attribute made
print(user2.subscriber)

# so now user2 has 3 attributes'''
#We can solve this problem as 
'''So there are ways that additional attributes cannot be added to an instance.
But you can select both.
They either allow to add the extra attributes or restrict them.'''