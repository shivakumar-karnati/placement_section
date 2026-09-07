# # math = 100

# # name = "shiva"

# # pi = 3.14

# # #check type
# # print(type(math))
# # print(type(name))
# # print(type(pi))

# # #check address

# # print(id(math))
# # print(id(name))
# # print(id(pi))


# # num = 123456
# # rev = 0
# # while num>0:
# #     last = num % 10
# #     rev = rev*10 +last
# #     num = num //10

# # print(rev)



# # val1 = int(input("enter num"))
# # val2 = int(input("enter num"))

# # print("before swap","val1 :",val1," val2 :",val2)

# # temp = val1
# # val1 = val2
# # val2 = temp

# # print("after swap","val1 :",val1," val2 :",val2)


# # # 3 subjects
# # maths = int(input("enter maths marks :"))
# # physics = int(input("enter physics marks :"))
# # chemistry = int(input("enter chemistry marks :"))

# # total = maths+physics+chemistry
# # print("total marks ",total)
# # percentage = total/3
# # print("percentage :",round(percentage,2))

# # if maths >= 40 and physics >=40 and chemistry >=40:
# #     print("pass")
# # else:
# #     print("fail")

# # if percentage >=60 and total >=100:
# #     print("eligible for placement")
# # else:
# #     print("not eligible for placement")


# # # charecter check

# # char = input("enter one charecter :")

# # if char.isupper():
# #     print("Upper case")
# # elif char.islower():
# #     print("lower")
# # elif char.isdigit():
# #     print("digit")
# # else:
# #     print("special")



# # #>>>>LIST AND SLICING OF ARRAY

# # list = [2,4,6,8,20]

# # print(list[0])
# # print(list[1:])
# # print(list[1:4])
# # print(list[-1])
# # print(list[0:4:2])
# # print(list[::-1])




# # # check no of even and odd numbers in list

# # list1 = [2,5,4,8,7,30,45,23,57,68]      #------>O(1)
# # e = 0
# # o = 0
# # for i in list1:                #------>O(n)
# #     if i%2 == 0:               #-------> O(1)
# #         e += 1                 #------->O(1)
# #     else:
# #         o += 1                 #--------> O(1)

# # print("even = ",e)              #--------> O(1)
# # print("odd = ",o)               #--------> O(1)
# # #--------->>>>>> TOTAL TIME COMPLEXITY  =>  O(1)+O(n) = O(n) <<<<<<<<---------





# # # -----------task 1  -------
# # # move zzeros in list to the last

# # list2 = [2,4,6,7,0,4,6,0,7]
# # print(list2)
# # for i in list2:
# #     if i == 0:
# #         list2.remove(i)
# #         list2.append(i)
# # print(list2)

# # #---- total time complexity  -> O(n)

# # # ----task 2 ---find max and min in list

# # list3 = [4,6,45,7,8,9,2]

# # print(max(list3))   #--------time complexity ->O(1)
# # print(min(list3))

# # mx = list3[0]
# # mn = list3[0]
# # for i in list3:
# #     if i >mx:
# #         mx = i
# #     if i < mn:
# #         mn = i
# # print(mx)
# # print(mn)
# # #------ time complexity -> O(n)



# # #---task 3 ----- second highest number

# # list4 = [2,4,5,6,34,5,6,37,35]
# # la=sl = list4[0]
# # for i in list4:
# #     if i>la:
# #         sl = la
# #         la = i
# #     elif i > sl and i != la:
# #         sl = i

# # print(sl)

# # #-----time complexity -> O(n)
# # list4.sort()
# # print(list4[-2])
# # #--- time complexity -> O(1)



# # #-----task -----
# # # product of all the elements except itself

# # l5 = [1,2,3,4]
# # p=1
# # ex = []
# # for i in range(len(l5)):    #----time complexity ->O(n)
# #     for j in l5:           #-----time cpmplexity -.O(n)
# #         p = p*j
# #     p = p//l5[i]
# #     ex.append(p)
# #     p = 1

# # print(ex)  
# # #-------total time complexity  O(n)*O(n) = O(n^2)





# # #------->FACTORIAL SOLUTION----------------------------------------------------------

# # def factorial(num):
# #     if num <= 1:
# #         return 1
# #     return num*factorial(num-1)

# # num = int(input("Enter number :"))
# # print(factorial(num))


# # #--------> power solution------------------------------------------------------------------->

# # def power(base,exponent):
# #     if exponent == 0:
# #         return 1
# #     return base * power(base,exponent-1)

# # base = int(input("Enter base number :"))
# # exponent = int(input("Enter exponenet number :"))

# # print(power(base,exponent))



# # #----------------poduct of array------------------------------------------------------------->

# # def productarray(list):
# #     if len(list) == 0:
# #         return 1
# #     return list[0] * productarray(list[1:])
# # list = [2,4,7,4,10]
# # print(productarray(list))




# # #---------Linearsearch----------------------------------------------------------------------------->

# # def linearsearch(arr,target):
# #     for i in range(len(arr)):
# #         if arr[i] == target:
# #             return i
# #     return -1



# # arr = [1,2,3,4,5,6,7,8,9]
# # target = 7
# # print(linearsearch(arr,target))



# #--count the highest consecutive 1s in binary numbers -------------------------->

# # def count_consicutive(s):
# #     count = 0
# #     maxcount = 0
# #     for i in s:
# #         if i == 1:
# #             count += 1
# #             maxcount = max(maxcount,count)
# #         else:
# #             count = 0
# #     return maxcount


# # s = [1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1]
# # print(count_consicutive(s))

 


#  #---------------------------------------------------------------------------
# # int() is used to convert into onteger
# # print(int(3.14))
# # print(int("44"))
# # print(int(True))
# # print(int(False))
# # print(int(10+2j))
# #  we can not convert the complex values into the int values 
# # we can not convert the string name to int values



# #----------------------------------------------------------------------------------------------------
# # float() is used to convert in to float values
# # print(float(3))
# # print(float(4))

# # we con not convert the string and complex values into the float values




# #----------------------------------------------------------------------------------
# # complex() is used to convert in to the complex values
# # we can convert anything to it except strings


# #------------------------------------------------------------------------------------------
# # bool() is used to convert onto boolean

# # it convert all the values except the strings



# #-----------------------task----------------
# # for i in range(1,6):
# #     if i == 3:
# #         pass
# #     else:
# #         print(i," ",6-i)



# #-----------------------------------------------------------------------------------
# #zip() is used to take multiple range in sinhle loop

# # for i,j in zip(range(1,6),range(5,0,-1)):
# #     if i == 3 and j == 3:
# #         continue
# #     print(i," ",j)





# #----------------------------------------------------------------------------------
# #constructor

# # class student:
# #     def __init__(self):
# #         print("i will called automatically")

# #     def message(self):
# #         print("inside the class")
# # obj = student()
# # obj.message()
# # print(obj)




# #--------------------------------------------------------------------------

# import sys
# class stack:
#     def __init__(self,stacksize):
#         self.stacksize = stacksize
#         self.stackList = []

#     def isfull(self):
#         if (len(self.stackList) == self.stacksize):
#             return True
#         else:
#             return False

#     def isEmpty(self):
#         if (self.stackList) == []:
#             return True
#         else:
#             return False

#     def push(self,data):
#         if self.isfull():
#             print("Stack is full")
#         else:
#             self.stackList.append(data)

#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             self.stackList.pop()

#     def peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.stackList[-1])
#     def deleteStack(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             self.stackList = None
#             print("stack is deleted")

#     def displaystack(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.stackList)

# size = int(input("Enter the size of stack :"))

# objstack = stack(size)

# while True:
#     print("1. push element    :")
#     print("2. pop element     :")
#     print("3. peek element    :")
#     print("4. isfull          :")
#     print("5. isempty         :")
#     print("6. delete stack    :")
#     print("7. display stack   :")
#     print("8. Exit            :")

#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("enter the value to push :"))
#         objstack.push(value)

#     elif choice == 2:
#         objstack.pop()

#     elif choice == 3:
#         objstack.peek()
#     elif choice == 4:
#         print(objstack.isfull())
#     elif choice == 5:
#         print(objstack.isEmpty())
#     elif choice == 6:
#         objstack.deleteStack()
#     elif choice == 7:
#         objstack.displaystack()
#     else:
#         sys.exit()




#--------------------------------------------------------------------------------------
#patterns

# n = int(input("enter the no of rows :"))
# for i in range(n,0,-1):
#     print(" "*(n-i),end=" ")
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()



#------------------------------------------------------------------------------------------
#string

# s = "shiva","kumar","karnati"
# m = '-'.join(s)
# print(m)



# s = "shiva kumar is good person"
# print(s.find("shiva"))
# print(s.find("bad"))  # if it is not there return -1
# print(s.find("person"))  # find it returns the staring insex number




# print('shiva123'.isalnum()) # True
# print('shiva'.isalnum()) # T
# print('a123'.isdigit()) #False
# print('shiva123'.isalnum()) #T
# print('shiva'.islower()) # T
# print(''.islower()) #F
# print('SHIVa123'.isupper()) #F
# print('SHIVA'.isupper()) #T
# print('My Name Is Shiva'.istitle()) #t
# print(''.istitle()) #F
# print(''.isspace()) #F
# print('Hello'.startswith("He")) #T
# print('Hello'.endswith("lo")) #T


#-----------------sclicing of string---------
# name = "shiva"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[-2])
# print(name[0:3])
# print(name[2:])
# print(name[:4])
# print(name[:])
# print(name[2:4])
# print(name[::-1])
# print(name[::-2])

# name = "shivakumar"
# for i in range(1,len(name)+1):
#     print(name[-i],end="")

#-------------------task------reverse string----
# name = "shivakumar"
# for i in range((len(name)-1),-1,-1):
#     print(name[i],end="")

#-------------------task----------- remove duplicates----

# name = "shivakumar"
# newname = ""
# for i in name:
#     if i not in newname:
#         newname += i

# print(newname)


#----------------taks------------------------check palindrome
# check with loop

# def palindrome(s):
#     for i in range(len(s)):
#         if s[i] == s[len(s)-1-i]:
#             return "palindrome"
#         else:
#             return "Not palindrome"

# s = input()
# print(palindrome(s))


#-------------------taks----------count vowel and consonants---------

# def counts(s):
#     vowels = ['a','e','i','o','u','A','E','I','O','U']
#     vc = 0
#     c = 0
#     for i in s:
#         if i in vowels:
#             vc += 1
#         else:
#             c += 1
#     print(vc,c)
            

# s = input()
# counts(s)

#-------task -------------- check anagram---

# def anagram(s1,s2):
#     if len(s1) == len(s2):
#         s1 = "".join(sorted(s1))
#         s2 ="".join(sorted(s2))
#         if s1[:] == s2[:]:
#             return "anagram"
#         else:
#             return "not anagram"
#     else:
#         return "not anagram"

# s1 = input()
# s2 = input()
# print(anagram(s1,s2))


#-------------task----count words in sentence----------

# var =" this is a sentence  "
# var1 = var.strip()
# count = 1
# for i in var:
#     if i == " ":
#         count +=1
# print(count)
#-----------------------
# var =" this is a sentence  "
# var1 = var.split()
# print(len(var1))


#-------------task -----------count special charecter in a message----------------------------------

# m = input()
# wh = 0
# sp = 0

# for i in m:
#     if i == " ":
#         wh += 1
#     a = ord(i)
#     if (a >=33 and a<=47) or (a>=58 and a<=64) or (a>=91 and a<=96) or (a>=123 and a<=126):
#         sp += 1

# print(wh)
# print(sp)


#-------task ---------- title case a sentence-------------

# t = input()
# print(t.title())




#----->>>Dictionary-------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# stu = {
#     101:"shiva",
#     102:"kumar",
#     "101":"karnati",
#     101:"bunny",
#     "name":"shiva"
# }
# # print(stu)

# for i in stu:
#     print(i)


# for i in stu.keys();
#     print(i)


# for i in stu.values():
#     print(i)


# for i in stu.items():
#     print(i)


# stu.pop(101)
# print(stu)


# stu.clear()
# print(stu)


# newstu = stu.copy()
# print(stu)
# print(newstu)


# print(stu[102])


# stu['color'] = 'black'
# print(stu)


#-------------Question----------------------
# write a program to accept student name and  marks from the keyboard and create a dictionary.
# Also display student marks by taking student name as input?


# n = int(input("Enter the number of students :"))
# d = {}
# for i in range(1,n+1):
#     name = input(f"{i}.Enter Student Name :")
#     marks = int(input(f"{i}.Enter Student marks :"))
#     d[name.lower()] = marks

# while True:
#     name = input("Enter student Name to get marks :")
#     marks = d.get(name.lower(),-1)
#     if marks == -1:
#         print("Student Not Found")
#     else:
#         print("The Marks of",name,"are",marks)
#     option = input("Do you want to find another Student Marks[Yes|No]")
#     if option.lower() == "No" or option.lower() == "no":
#         break

# print("Thanks for using our application")



#--------task---------------------------

# a = {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])             #(4,5) this si a single so execute


# a = {'a':1,'b':2,'c':3}
# print(a['a','b'])        #[a,b] these are two separate keys we con not access at time two keyss



# f = {}
# def addone(index):
#     if index in f:
#         f[index] += 1
#     else:
#         f[index] = 1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print(f)


# di = {}
# di[(1,2,3)] = 8
# di[(2,3)] = 10
# di[(3,4)] = 20

# print(di)


# box = {}
# create ={}
# create['box'] = box
# print(len(create['box']))


# box = {}
# create ={}
# create['box'] = box
# print(len(create[box]))


# dict = {'c':97,'a':96,'b':98}
# print(sorted(dict))         #sorted function is sorted by the key value not by the value



#------------------------QUEUE-------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.----------------------------------------

# import sys

# class Queue:

#     def __init__(self,queuesize):
#         self.queuesize = queuesize
#         self.queueList = []

#     def isempty(self):
#         if len(self.queueList) == 0:
#             return True
#         else:
#             return False

#     def isfull(self):
#         if len(self.queueList) == self.queuesize:
#             return True
#         else:
#             return False

#     def enQueue(self,value):
#         self.data = value
#         if self.isfull():
#             print("Queue is Full")
#         else:
#             self.queueList.append(value)
#             print(self.queueList[-1],"is added")

#     def deQueue(self):
#         if self.isempty():
#             print("Queue is empty")
#         else:
#             print(self.queueList[0], " is deleted")
#             self.queueList.pop(0)
            

#     def peekFront(self):
#         if self.isempty():
#             print("Queue is empty")
#         else:
#             print(self.queueList[0])

#     def displayqueue(self):
#         if self.isempty():
#             print("Queue is empty")
#         else:
#             print(self.queueList)

#     def deleteQueue(self):
#         if self.isempty():
#             print("Queue is empty")
#         else:
#             self.queueList = None
#             print("Queue deleted")



# size = int(input("Enter the sizze of Queue :"))
# queueobj = Queue(size)

# while True:
#     print("1. enQueue element      :")
#     print("2. deQueue element      :")
#     print("3. peekfront element    :")
#     print("4. isfull               :")
#     print("5. isempty              :")
#     print("6. delete Queue         :")
#     print("7. display Queue        :")
#     print("8. Exit                 :")

#     choice = int(input("Enter your choice :"))
#     if choice == 1:
#         value = int(input("enter the value to push :"))
#         queueobj.enQueue(value)

#     elif choice == 2:
#         queueobj.deQueue()

#     elif choice == 3:
#         queueobj.peekFront()
#     elif choice == 4:
#         print(queueobj.isfull())
#     elif choice == 5:
#         print(queueobj.isempty())
#     elif choice == 6:
#         queueobj.deleteQueue()
#     elif choice == 7:
#         queueobj.displayqueue()
#     else:
#         sys.exit()


# >>>>>>>>>>-------------------------------------------------------------------------

# class Employee:
#     def __init__(self):
#         self.name = "shiva kumar"  #instance var


# obj1 = Employee() #["shiva kumar"]
# obj2 = Employee() #["shiva kumar"]
# obj3 = Employee() #["shiva kumar"]
# print(obj1.name)
# print(obj2.name)  # each object takes seperate memory
# print(obj3.name)

# obj1.name = "karnati"  # we can assign the values with objects
# obj2.name = "bunny"

# print(obj1.name)
# print(obj2.name)
# print(obj3.name)


#>>>>>>>>>>>>.--------------------------------------------------------------------
#acccessing nad seleting instance variable form the class

# class student:
#     def __init__(self):
#         self.name = "shiva" #instance
#         self.rollno = 101

#     def getdata(self):
#         self.mb = 987654321

# obj = student()
# obj.getdata()
# obj.branch = "cse"  #adding instance variable by usong object
# del obj.rollno      # deleting a instance variabel through the del key
# print(obj.__dict__)


#--------------------------------->>>>>>>STATIC VARIABLE>>>>>>>>>>>>>>>----------------------------------
#staic variable

# class college:
#     college_name = "sandip university"

# obj1 = college()
# obj2 = college()
# obj3 = college()

# print(obj1.college_name)  #"sandip unniversity"
# print(obj2.college_name)
# print(obj3.college_name)

# college.college_name = "lpu university"  # can change the whole memory of the variable with calss name

# print(obj1.college_name)  #lpu university"
# print(obj2.college_name)
# print(obj3.college_name)




#----------------------------------------------------LINKED LIST-------------------------------------------->>>>>>>>>>>>>>>>>
#LINKED LIST
# linked list is a form of a sequentail collection and it does not have to be in order. 
# A linked liat is made up of independent nodes that may contains any type of data and 
# each node has a reference to the nextnnode in the link.

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