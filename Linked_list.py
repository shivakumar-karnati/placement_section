#----------------------------------------------------LINKED LIST-------------------------------------------->>>>>>>>>>>>>>>>>
#LINKED LIST
# linked list is a form of a sequentail collection and it does not have to be in order. 
# A linked liat is made up of independent nodes that may contains any type of data and 
# each node has a reference to the nextnnode in the link.

#static linked list  

class Node:   #this is n=only for create a independent node
    def __init__(self,value):
        self.data = value    #[10|102]->[20|103]->[30|none]
        self.next = None      #   101       102     103

class LinkedList:
    def __init__(self):
        self.head = None   #[None]


linkedobj = LinkedList()  

# creating independent nodes
linkedobj.head = Node(10)  #101
second         = Node(20)   #102
third          = Node(30)   #103
fourth         = Node(40)


#connection nodes
linkedobj.head.next = second
second.next = third
third.next = fourth


#display linkedlist

while linkedobj.head != None:
    print("[",linkedobj.head.data,"|",linkedobj.head.next,"]","->",end="")
    linkedobj.head = linkedobj.head.next



# dynamic linked list

class Node:
    def __init__(self,value):
        self.data = value  #[10|None]   [5|none]
        self.Next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeBeginning(self,value):
        nodeValue = Node(value)

        if self.head is None:
            self.head = nodeValue
            self.tail = nodeValue
        else:
            nodeValue.Next = self.head
            self.head = nodeValue


    def addNoteEnd(self,value):
        nodevalue = Node(value)
        if self.head is None:
            self.head = nodevalue
            self.tail = nodevalue

        else:
            self.tail.Next = nodevalue
            self.tail = nodevalue
    # def addInBetween(self,place,value):


    def display(self):
        while self.head != None:
            print("[",self.head.data,"|","]","->",end="")
            self.head = self.head.Next
        


linked_obj = LinkedList()
linked_obj.addNodeBeginning(10)
linked_obj.addNodeBeginning(5)
linked_obj.addNodeBeginning(50)

linked_obj.addNoteEnd(20)
linked_obj.addNoteEnd(30)

linked_obj.display()



import sys

#----------------------Single LinkedList----------------------------------------

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeBegining(self,value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head = node

    def addNodeAtEnd(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

    def addNodeInBetween(self,beforeNode,value):
        node = Node(value)
        if self.head is None:
            print("The List is Empty")
            return
        
        temp = self.head
        while temp and temp.data != beforeNode:
            temp = temp.next
        
        if temp is None:
            print("Before Node Not Found")
        node.next = temp.next
        temp.next = node

        if temp == self.tail:
            self.tail = temp


    def delNode(self,value):
    
        temp = self.head
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if temp is None:
            print("Node not found")
            return
        
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        if temp == self.tail:
            self.tail = prev

    def displayLinkedList(self):
        if self.head is None:
            print("LinkedList is Empty")
            return
        temp = self.head
        while temp is not None:
            print(temp.data,end="->")
            temp = temp.next
        print("Null")

l_obj = linkedlist()
while True:
    print("1. Add a Node at Begining")
    print("2. Add a Node at End")
    print("3. Add a Node InBetwenn")
    print("4. Delete a Node")
    print("5. Display the LinkedList")
    print("6. Exit")

    option = int(input("Enter The Option :"))
    if option == 1:
        value = int(input("Enter The Node :"))
        l_obj.addNodeBegining(value)
    elif option == 2:
        value = int(input("Enter The Node :"))
        l_obj.addNodeAtEnd(value)
    elif option == 3:
        beforeNode = int(input("Enter the before node you want to add :"))
        value = int(input("Enter the node :"))
        l_obj.addNodeInBetween(beforeNode,value)

    elif option == 4:
        value = int(input("Enter The Node :"))
        l_obj.delNode(value)

    elif option == 5:
        l_obj.displayLinkedList()
    elif option == 6:
        sys.exit()

    else:
        print("Enter the valid Option")





#-------------------------------------Double LinkedList--------------------------------

class Node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None

class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNodeEnd(self,value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
    def displayDoubleLL(self):
        if self.head is None:
            print("list is Empty ")
            return
        temp = self.head
        while temp :
            print(temp.data,end="<=>")
            temp = temp.next
        print("NUll")
            


obj_dll = doubleLinkedList()
obj_dll.insertNodeEnd(10)
obj_dll.insertNodeEnd(30)
obj_dll.insertNodeEnd(50)
obj_dll.displayDoubleLL()



#---------------------------------->>Circular LinkedList >>>>---------------------------------------
#circular linked list

class Node:

    def __init__(self,value):
        self.data = value
        self.next = None

class ciculerLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def addNodeAtEnd(self,value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            self.tail.next = self.head

        else:
            self.tail.next = node
            self.tail = node
            self.tail.next = self.head

    def displayCircularLL(self):
        if self.head is None:
            print("list is empty ")
            return

        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

obj_CLL = ciculerLinkedList()
obj_CLL.addNodeAtEnd(10)
obj_CLL.addNodeAtEnd(20)
obj_CLL.addNodeAtEnd(30)

obj_CLL.displayCircularLL()


