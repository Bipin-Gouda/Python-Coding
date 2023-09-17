class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
        else:
            ptr=self.head
            while ptr.next:
                ptr=ptr.next
            ptr.next=Node(data,None)
            
    
    def ReverseLL(self):
        current=self.head
        nextnode=None
        prev=None
        while current:
            nextnode=current.next
            current.next=prev
            prev=current
            current=nextnode
        self.head=prev
        
            
    def print(self):
        if self.head is None:                                  # Empty LL
            print('LinkedList is Empty')
            return
        
        ptr=self.head                                          # Non Empty LL
        while ptr:
            print(ptr.data,end=" ")
            ptr=ptr.next
        print()
            

if __name__ == '__main__':
    ll=LinkedList()                                       # in ML model=DecisionttreeRegressor() -> ceating object of a class
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_at_end(8)
    ll.print()
    ll.ReverseLL()
    ll.print()
    
