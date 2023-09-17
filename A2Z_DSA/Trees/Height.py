class Node:
    def __init__(self,data):                 # Creation of a node
        self.data=data
        self.leftChild=None
        self.rightChild=None
        
    def insert(self,data):
        if data < self.data:
            if self.leftChild:                  # Recursion to the left 
                self.leftChild.insert(data)
            else:
                self.leftChild=Node(data)
                return
        else:
            if self.rightChild:
                self.rightChild.insert(data)
            else:
                self.rightChild=Node(data)
                return
            
   
    
def height(root):
         # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
     return 0 
      # Recursively call height of each node
    leftAns = height(root.leftChild)
    rightAns = height(root.rightChild)
 
      # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1
                          
        
# Creating root node
root = Node(27)                                           # root is a obj of class Node here
# Inserting values in BST
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.insert(5)
root.insert(1)
# searching the values
#print(root.search(7))
#print(root.search(14))
print(height(root))

    