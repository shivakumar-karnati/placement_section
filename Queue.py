
#------------------------QUEUE-------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.----------------------------------------

import sys

class Queue:

    def __init__(self,queuesize):
        self.queuesize = queuesize
        self.queueList = []

    def isempty(self):
        if len(self.queueList) == 0:
            return True
        else:
            return False

    def isfull(self):
        if len(self.queueList) == self.queuesize:
            return True
        else:
            return False

    def enQueue(self,value):
        self.data = value
        if self.isfull():
            print("Queue is Full")
        else:
            self.queueList.append(value)
            print(self.queueList[-1],"is added")

    def deQueue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.queueList[0], " is deleted")
            self.queueList.pop(0)
            

    def peekFront(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.queueList[0])

    def displayqueue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            print(self.queueList)

    def deleteQueue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            self.queueList = None
            print("Queue deleted")



size = int(input("Enter the sizze of Queue :"))
queueobj = Queue(size)

while True:
    print("1. enQueue element      :")
    print("2. deQueue element      :")
    print("3. peekfront element    :")
    print("4. isfull               :")
    print("5. isempty              :")
    print("6. delete Queue         :")
    print("7. display Queue        :")
    print("8. Exit                 :")

    choice = int(input("Enter your choice :"))
    if choice == 1:
        value = int(input("enter the value to push :"))
        queueobj.enQueue(value)

    elif choice == 2:
        queueobj.deQueue()

    elif choice == 3:
        queueobj.peekFront()
    elif choice == 4:
        print(queueobj.isfull())
    elif choice == 5:
        print(queueobj.isempty())
    elif choice == 6:
        queueobj.deleteQueue()
    elif choice == 7:
        queueobj.displayqueue()
    else:
        sys.exit()

