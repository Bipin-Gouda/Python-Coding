# Creating node class
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Function to insert in BST
    def insert(self, data):
        # if value is lesser than the value of the parent node
        if data < self.data:
            if self.leftChild:
                # if we still need to move towards the left subtree
                self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return
        # if value is greater than the value of the parent node        
        else:
            if self.rightChild:
                # if we still need to move towards the right subtree
                self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return
       
            
    # function to Traverse (Print) a BST
            
    def Preorder(self):
        print(self.data,end=" ")
        if self.leftChild:
            self.leftChild.Preorder()
        if self.rightChild:
            self.rightChild.Preorder()
    
    def Inorder(self):                                  
        if self.leftChild:
            self.leftChild.Inorder()
        print( self.data, end=" ")
        if self.rightChild:
            self.rightChild.Inorder()
            
    def Postorder(self):
        if self.leftChild:
            self.leftChild.Postorder()
        if self.rightChild:
            self.rightChild.Postorder()
        print(self.data,end=" ")
          


# Creating root node
root = Node(27)                                           # root is a obj of class Node here
# Inserting values in BST
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
# searching the values
#print(root.search(7))
#print(root.search(14))
root.Preorder()            
print()
root.Inorder()
print()
root.Postorder()
print()


# Debugged and verified works fine
# These functions (Preorder, Postorder, Inorder) can ben written outside class as well we just need to pass root then