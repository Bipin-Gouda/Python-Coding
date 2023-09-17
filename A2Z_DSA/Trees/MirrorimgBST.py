# A class to store a binary tree node 
class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
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
            
 
 
# Function to perform preorder traversal on a given binary tree
def preorder(root):
    if root is None:
        return
 
    print(root.data, end=' ')
    preorder(root.leftChild)
    preorder(root.rightChild)
 
 
# Utility function to swap left subtree with right subtree
def swap(root):
    if root is None:
        return
 
    temp = root.leftChild
    root.leftChild = root.rightChild
    root.rightChild = temp
 
 
# Function to convert a given binary tree into its mirror
def convertToMirror(root):
 
    # base case: if the tree is empty
    if root is None:
        return
 
    # convert left subtree
    convertToMirror(root.leftChild)
 
    # convert right subtree
    convertToMirror(root.rightChild)
 
    # swap left subtree with right subtree
    swap(root)
 
 
if __name__ == '__main__':
 
    ''' Construct the following BST tree (then do mirror)
              5
            /   \
           /     \
          2       6
         / \       \
        1   3       7
             \
              4   
    '''
 
    root = Node(5)
    root.insert(2) 
    root.insert(3)     
    root.insert(4) 
    root.insert(1)
    root.insert(6)
    root.insert(7)
    
    preorder(root)
    print()
    convertToMirror(root)
    preorder(root)