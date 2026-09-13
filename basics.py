math = 100
name = "shiva"
pi = 3.14

#check type
print(type(math))
print(type(name))
print(type(pi))

#check address

print(id(math))
print(id(name))
print(id(pi))

#------------------------------------------------------------------------------------------------

# if - else statements

# 3 subjects
maths = int(input("enter maths marks :"))
physics = int(input("enter physics marks :"))
chemistry = int(input("enter chemistry marks :"))

total = maths+physics+chemistry
print("total marks ",total)
percentage = total/3
print("percentage :",round(percentage,2))

if maths >= 40 and physics >=40 and chemistry >=40:
    print("pass")
else:
    print("fail")

if percentage >=60 and total >=100:
    print("eligible for placement")
else:
    print("not eligible for placement")

#-------------------------------------------------------------------------------------------

# charecter check

char = input("enter one charecter :")

if char.isupper():
    print("Upper case")
elif char.islower():
    print("lower")
elif char.isdigit():
    print("digit")
else:
    print("special")

#-----------------------------------------------------------------------------------------------
#>>>>LIST AND SLICING OF ARRAY

list = [2,4,6,8,20]

print(list[0])
print(list[1:])
print(list[1:4])
print(list[-1])
print(list[0:4:2])
print(list[::-1])


#----------------poduct of array------------------------------------------------------------->

def productarray(list):
    if len(list) == 0:
        return 1
    return list[0] * productarray(list[1:])
list = [2,4,7,4,10]
print(productarray(list))


#  #---------------------------------------------------------------------------------------------
int() #is used to convert into onteger
print(int(3.14))
print(int("44"))
print(int(True))
print(int(False))
print(int(10+2j))
#  we can not convert the complex values into the int values 
# we can not convert the string name to int values



# ----------------------------------------------------------------------------------------------------
float() #is used to convert in to float values
print(float(3))
print(float(4))

# we con not convert the string and complex values into the float values




# #----------------------------------------------------------------------------------
complex() #is used to convert in to the complex values
# we can convert anything to it except strings


#------------------------------------------------------------------------------------------
bool() #is used to convert onto boolean

# it convert all the values except the strings


# #-----------------------------------------------------------------------------------
zip() #is used to take multiple range in sinhle loop

for i,j in zip(range(1,6),range(5,0,-1)):
    if i == 3 and j == 3:
        continue
    print(i," ",j)


#--------------------------------------------------------------------------------------------
#constructor         when object is created constructor called automatically

class student:
    def __init__(self):
        print("i will called automatically")

    def message(self):
        print("inside the class")
obj = student()
obj.message()
print(obj)


#--------------------------------------------------------------------------------------
#patterns

n = int(input("enter the no of rows :"))
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
    print()




#-------------------------------------------------------------------------------------------------
a = {(1,2):1,(2,3):2,(4,5):3}
print(a[4,5])             #(4,5) this is a single so execute


a = {'a':1,'b':2,'c':3}
print(a['a','b'])        #[a,b] these are two separate keys we con not access at time two keyss



f = {}
def addone(index):
    if index in f:
        f[index] += 1
    else:
        f[index] = 1
addone('Apple')
addone('Banana')
addone('apple')
addone('Apple')
print(f)


di = {}
di[(1,2,3)] = 8
di[(2,3)] = 10
di[(3,4)] = 20

print(di)


box = {}
create ={}
create['box'] = box
print(len(create['box']))


box = {}
create ={}
create['box'] = box
print(len(create[box]))


dict = {'c':97,'a':96,'b':98}
print(sorted(dict))         #sorted function is sorted by the key value not by the value



# >>>>>>>>>>-----------------------------------------------------------------------------------
# ---- class and object---------------------------
class Employee:
    def __init__(self):
        self.name = "shiva kumar"  #instance var


obj1 = Employee() #["shiva kumar"]
obj2 = Employee() #["shiva kumar"]
obj3 = Employee() #["shiva kumar"]
print(obj1.name)
print(obj2.name)  # each object takes seperate memory
print(obj3.name)

obj1.name = "karnati"  # we can assign the values with objects
obj2.name = "bunny"

print(obj1.name)
print(obj2.name)
print(obj3.name)


#>>>>>>>>>>>>.--------------------------------------------------------------------
#acccessing nad seleting instance variable form the class

class student:
    def __init__(self):
        self.name = "shiva" #instance
        self.rollno = 101

    def getdata(self):
        self.mb = 987654321

obj = student()
obj.getdata()
obj.branch = "cse"  #adding instance variable by usong object
del obj.rollno      # deleting a instance variabel through the del key
print(obj.__dict__)


#--------------------------------->>>>>>>STATIC VARIABLE>>>>>>>>>>>>>>>----------------------------------
#staic variable

class college:
    college_name = "sandip university"

obj1 = college()
obj2 = college()
obj3 = college()

print(obj1.college_name)  #"sandip unniversity"
print(obj2.college_name)
print(obj3.college_name)

college.college_name = "lpu university"  # can change the whole memory of the variable with calss name

print(obj1.college_name)  #lpu university"
print(obj2.college_name)
print(obj3.college_name)



#-------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>TUPLE---------------->>>>>>>>>>>>>>>>>>>>>>>>>>.
#tuple is a immutable so it can't change the value

tuple_a = 'a','b'
tuple_b = ('a','b')
print(tuple_a == tuple_b)


# --------------------------------------------

t_a = '1','2'
t_b = ('3','4')

print(t_a+t_b)

#--------------------------------------------

l = [1,2,3]
t = ('python',)*(l.__len__() - l[::-1][0])
print(t)

#--------------------------------------

t = ('python',)*3
print(type(t))

# -------------------------------------------------

t = (1,)*3
t[0] = 2  
print(t)

#-----------------------------------------

t = ((1,2),)*7
print(len(t[3:8]))
