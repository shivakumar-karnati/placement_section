
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
        if self.head == None:
            self.head = nodevalue
            self.tail = nodevalue

        else:
            self.tail.Next = nodevalue
            self.tail = nodevalue
    # def addInBetween(self,place,value):


    def display(self):
        while self.head != None:
            print("[",self.head.data,"|",self.head.Next,"]","->",end="")
            self.head = self.head.Next
        


linked_obj = LinkedList()
linked_obj.addNodeBeginning(10)
linked_obj.addNodeBeginning(5)
linked_obj.addNodeBeginning(50)

linked_obj.addNoteEnd(20)
linked_obj.addNoteEnd(120)

linked_obj.display()