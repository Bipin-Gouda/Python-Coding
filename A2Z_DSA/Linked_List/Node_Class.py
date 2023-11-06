# used to create an individual node   # self points to the current object itself, we do self.value b/c remember to create a new attribute we do object.attribute=data
#cookie1.weight=10   creates an attribute weight for cookie1 with value 10
class Node:
    def __init__(self,value,):
        self.value=value
        self.next=None                    #initially next is None as we dont know its left/right the LL Class will handle those 


'''
newnode=Node(10)
print(newnode.value,newnode.next)
'''

'''
class LinkedList:
    def __init__(self,value):
        newnode=Node(value)
        self.head=newnode                
        self.tail=newnode
        self.length=1                 # as we have only made one node in LL now
'''
class LinkedList:
    def __init__(self):                     #empty LL
        self.head=None
        self.tail=None
        self.length=0

newnode=LinkedList()
print(newnode.length)