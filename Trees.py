
# --------------------->>>>>>>>>>>>>>>>>>>>>>>>>>---TRESS-------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>----------------------
# trees

class Tree:
    def __init__(self,data):
        self.data = data
        self.tree_list = []

    def addchild(self,child):
        self.tree_list.append(child)


    def __str__(self,level = 0):   ## when obj is print it called automatically
                        
        ret = " "* level + str(self.data) + "\n"
        for child in self.tree_list:
            ret += child.__str__(level+1)
        return ret
    
rootObj = Tree("Drinks")
hot     = Tree("Hot")
cold    = Tree("Cold")

rootObj.addchild(hot)
rootObj.addchild(cold)


tea = Tree("tea")
coffee = Tree("coffee")
hot.addchild(tea)
hot.addchild(coffee)

nonalchohalic = Tree("Non Alchohalic")
alchohalic = Tree("Alchohalic")

cold.addchild(nonalchohalic)
cold.addchild(alchohalic)
print(rootObj)
print(hot)
print(cold)




#-------------------------->>>>>> TREES >>>>>>> ----------------------------------------------------------
# BINARY SEARCH TREE

class Node:

    def __init__(self,value):
        self.data = value
        self.leftChild = None
        self.rightChild = None

class binarySearchTree:

    def __init__(self):
        self.root = None

    def insertNode(self,rootNode,nodevalue):

        if rootNode is None:
            return Node(nodevalue)

        elif rootNode.data >= nodevalue:
            if rootNode.leftChild is None:
                rootNode.leftChild = Node(nodevalue)
            else:
                self.insertNode(rootNode.leftChild,nodevalue)

        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = Node(nodevalue)
            else:
                self.insertNode(rootNode.rightChild,nodevalue)

        return rootNode

    def preOrder(self,rootNode):
        if rootNode is None:
            return

        
        print(rootNode.data,end=" ")
        self.preOrder(rootNode.leftChild)
        self.preOrder(rootNode.rightChild)

    def inOrder(self,rootNode):
        if rootNode is None:
            return

        
        self.preOrder(rootNode.leftChild)
        print(rootNode.data,end=" ")

        self.preOrder(rootNode.rightChild)
    def postOrder(self,rootNode):
        if rootNode is None:
            return

        
        self.preOrder(rootNode.leftChild)
        self.preOrder(rootNode.rightChild)
        print(rootNode.data,end=" ")


    def deleteNode(self,rootNode):
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None

        return "The BST has been successfully deleted"


    def searchNode(self,rootNode,nodeValue):
        if rootNode.data == nodeValue:
            print("The value is found")

        elif nodeValue < rootNode.data:
            if rootNode.leftChild.data == nodeValue:
                print("The value is found")
            else:
                self.searchNode(rootNode.leftChild,nodeValue)
        else:
            if rootNode.rightChild.data == nodeValue:
                print("The value is found")
            else:
                self.searchNode(rootNode.rightChild,nodeValue)


bst = binarySearchTree()

bst.root = bst.insertNode(bst.root,50)
bst.root = bst.insertNode(bst.root,30)
bst.root = bst.insertNode(bst.root,70)
bst.root = bst.insertNode(bst.root,20)
bst.root = bst.insertNode(bst.root,40)
bst.root = bst.insertNode(bst.root,60)
bst.root = bst.insertNode(bst.root,80)

bst.preOrder(bst.root)
    

    
