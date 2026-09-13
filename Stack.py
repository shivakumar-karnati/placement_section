
#---------------------------------------------------------------------------------

import sys
class stack:
    def __init__(self,stacksize):
        self.stacksize = stacksize
        self.stackList = []

    def isfull(self):
        if (len(self.stackList) == self.stacksize):
            return True
        else:
            return False

    def isEmpty(self):
        if (self.stackList) == []:
            return True
        else:
            return False

    def push(self,data):
        if self.isfull():
            print("Stack is full")
        else:
            self.stackList.append(data)

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            self.stackList.pop()

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.stackList[-1])
    def deleteStack(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.stackList = None
            print("stack is deleted")

    def displaystack(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.stackList)

size = int(input("Enter the size of stack :"))

objstack = stack(size)

while True:
    print("1. push element    :")
    print("2. pop element     :")
    print("3. peek element    :")
    print("4. isfull          :")
    print("5. isempty         :")
    print("6. delete stack    :")
    print("7. display stack   :")
    print("8. Exit            :")

    choice = int(input("Enter your choice :"))
    if choice == 1:
        value = int(input("enter the value to push :"))
        objstack.push(value)

    elif choice == 2:
        objstack.pop()

    elif choice == 3:
        objstack.peek()
    elif choice == 4:
        print(objstack.isfull())
    elif choice == 5:
        print(objstack.isEmpty())
    elif choice == 6:
        objstack.deleteStack()
    elif choice == 7:
        objstack.displaystack()
    else:
        sys.exit()



