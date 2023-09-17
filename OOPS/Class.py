class Dog:
    
    # Class attribute
    species = "Canis familiaris"
    
    def __init__(self, name, age):              # only class methods and constructors require self 
        self.name = name                    # instance attributes 
        self.age = age
    
     # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

class JackRussellTerrier(Dog):           # Inheritance
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


        
buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print(buddy.name)
print(miles.age)
print(miles.species)

print(miles.description())
print(miles.speak("woof"))

print(miles)                  # <__main__.Dog object at 0x000001DB4C30CC90>   o/p
                              #  Miles is 4 years old