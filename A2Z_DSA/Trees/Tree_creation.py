# This is a General tree not a Binary Tree

class TreeNode:
    def __init__(self, data, children=[]):
        self.data=data
        self.children=children

    def __str__(self, level=0):                  #str function for tree
        ret= " " * level +str(self.data) + "\n"
        for child in self.children:
            ret+= child.__str__(level+1)
        return ret
    
    def addChild(self, child):
        self.children.append(child)

    def addChildren(self, children):   # can add single or multiple children at once
        self.children.extend(children)

drinks = TreeNode('Drinks')
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])
drinks.addChild(cold)   # list of objects
drinks.addChild(hot)
#print(drinks)
tea = TreeNode('tea',[])
coffee = TreeNode('coffee',[])
cola = TreeNode('cola',[])
fanta = TreeNode('fanta',[])
hot.addChildren([tea,coffee])
#hot.addChild(coffee)
cold.addChildren([cola,fanta])
#cold.addChild(fanta)
print(drinks)  # what the print function will do when an object is called is specified
