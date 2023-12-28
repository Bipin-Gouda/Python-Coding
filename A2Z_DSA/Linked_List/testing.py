# Creating Node class
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
# Creating Linked List class
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
            
    def del_frm_beginning(self):
        if self.head is None:
            print("Nothing to delete")
            return
        else:
            ptr=self.head
            self.head=self.head.next
            del ptr
            
    def del_from_end(self):                           
        if self.head is None:
            print("Nothing to delete")
            return
        else:
            ptr=self.head
            ptrx=ptr
            while ptr.next:                            # had to sve both ptr ,ptr.next
                currentptr=ptr
                ptr=ptr.next
            temp=ptr
            currentptr.next=None
            del temp

    
    def search_ele(self,element):
        if self.head is None:
            print("LL is empty")
            return
        else:
            ptr=self.head
            c=0
            while(ptr):
                c+=1
                if(ptr.data==element):
                    print("Element found at position {}".format(c))
                    return
                ptr=ptr.next
            return
        
    def deleteDuplicates(self):
        # TODO
        temp=self.head
        while(temp!=None):
            t2=temp
            while t2.next!=None and t2.data==t2.next.data:              #sliding window
                t2=t2.next
            temp.next=t2.next
            temp=temp.next
        return self.head
    
    def removeElements(self,val):
        # TODO
        prev=self.head
        if prev==None:
            return self.head
        curr=prev.next
        while(curr!=None):
            if curr.data==val:
                prev.next=curr.next
                curr=curr.next
            else:
                prev=curr
                curr=curr.next
        if self.head.data==val:
            self.head=self.head.next
        return self.head
            
        
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
    ll.insert_at_beginning(1)
    #ll.insert_at_beginning(1)
    #ll.insert_at_beginning(7)
    ll.insert_at_end(1)
    ll.insert_at_end(1)
    ll.insert_at_end(1)
    ll.insert_at_end(7)
    ll.insert_at_end(7)
    ll.insert_at_end(7)
    ll.print()
    #ll.del_frm_beginning()
    ll.removeElements(7)
    #ll.print()
    #ll.del_from_end()
    #ll.deleteDuplicates()
    ll.print()



