class Treenode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    
newBt=Treenode('Drinks')  # or numeic value
l1=Treenode('Cold')
r1=Treenode('Hot')
newBt.left=l1
newBt.right=r1
cl2=Treenode('cola')
cr2=Treenode('fanta')
l1.left=cl2
l1.right=cr2
print(newBt)

