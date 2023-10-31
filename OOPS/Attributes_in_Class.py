'''
class StarCookie:
    pass

cookie1=StarCookie()
cookie1.color='orange'
cookie1.weight=15
cookie2=StarCookie()    # we can initialise attributes this way but doing it for each attribute is very time taking so we use initializer
cookie2.color='red'
cookie2.weight=20
print(cookie2.color)
'''

###  Using Initializer to initialize objects

class StarCookie:
    milk=0.1

    def __init__(self,color,weight):             # self is the object, object itself passed to the init, init is the constructor in python
        self.color=color                  # cookie2.color='red' ,cookie2 is object here self is object                 
        self.weight=weight

cookie1=StarCookie('red',15)
print(cookie1.color)
print(cookie1.weight)
cookie2=StarCookie('Yellow',16)

# so this is more convenient as now we dont have to initialise attributes for each object we can just pass them as parameters
'''
There might be attributes that all instances share and their value is the same.
So in this case we can use the class attribute.
'''

# Till now the attributes we saw were object attributes but there is a possible way to use class attributes as well
'''
The class attribute is similar to global variable for the class itself.
So if I go ahead and create over here class attribute before this init function, this is going to be
applicable for all objects and for everything that we have in our class.
So let's say for Cookie, we also need milk. 0.1L
'''

print(cookie1.milk)
print(cookie2.milk)
print(StarCookie.milk)

# Namespace dictionary (what belongs to object, what to class )


print(cookie1.__dict__)
print(cookie2.__dict__)
print(StarCookie.__dict__)   # milk belongs to class not the objects as we see in output but the objr=ects can access it

'''
So you can think of namespace as a dictionary in which keys are the objects
Names and values are the objects themselves.So this is going to return the attributes and methods of the instance of the class.
'''

cookie1.milk=0.2

# value only changes for cookie1

#StarCookie.milk=0.2   # values change for all

print(cookie1.milk)
print(cookie2.milk)
print(StarCookie.milk)



"""
So this means that whenever you are setting the milk class attribute for the object itself, it's going
to override the class attribute and it will add this attribute to the object's attribute itself 
"""

print(cookie1.__dict__)
print(cookie2.__dict__)
print(StarCookie.__dict__) 