#-------------Question-1---------------------------------------------------------------
# write a program to accept student name and  marks from the keyboard and create a dictionary.
# Also display student marks by taking student name as input?


n = int(input("Enter the number of students :"))
d = {}
for i in range(1,n+1):
    name = input(f"{i}.Enter Student Name :")
    marks = int(input(f"{i}.Enter Student marks :"))
    d[name.lower()] = marks

while True:
    name = input("Enter student Name to get marks :")
    marks = d.get(name.lower(),-1)
    if marks == -1:
        print("Student Not Found")
    else:
        print("The Marks of",name,"are",marks)
    option = input("Do you want to find another Student Marks[Yes|No]")
    if option.lower() == "No" or option.lower() == "no":
        break

print("Thanks for using our application")


#---------QUESTOION ----------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 # WAP to accespt rating in float and increment the salary based 
 # on rating like the test cases given below.

salary = int(input("Enter your salary :"))
rating = float(input("Enter the rating :"))
if rating <= 5 and rating >= 0:

    if rating >=1 and rating <=3:
        print("original salary :",salary)
        print("Salary increment by 10 %")
        print("increment :",(salary/100)*10)
        print("increment salary : ",((salary/100)*10)+salary)

    elif rating >=3.1 and rating <= 4:
        print("original salary :",salary)
        print("Salary increment by 20 %")
        print("increment :",(salary/100)*20)
        print("increment salary : ",((salary/100)*20)+salary)

    elif rating >=4.1 and rating <= 5:
        print("original salary :",salary)
        print("Salary increment by 30 %")
        print("increment :",(salary/100)*30)
        print("increment salary : ",((salary/100)*30)+salary)
else:
    print("Enter the rating in between 0-5")



# ---->>>>>>>>>>>>>>> COMPANY QUESTIONS ------------------>>>>>>>>>>>>>>>

# Q - 1-----------------------------------------------
#count special char in string
digits = str(int(input()))
spe_digit = str(int(input()))

print(digits.count(spe_digit))


# Q - 2------------------------------------------------------------------------
#display 1st evens and next odds in a list
n = int(input())
list = list(map(int, input().split()))[:n]
even = []
odd = []
for i in list:
    if i %2 != 0:
        odd.append(i)
    else:
        even.append(i)

print(even+odd)


# Q - 3-------------------------------------------------------------------
# print the sum of the max productions of 2 numbers
# 1 - approach----------------------

n= int(input())

values = list(map(int, input().split()))[:n]

maxpro = 0
card1 = 0
card2 = 0
for i in range(len(values)-1):
    for j in range(i+1,len(values)):
        pro = values[i]*values[j]
        if maxpro < pro:
            maxpro = pro
            card1 = values[i]
            card2 = values[j]

print(card1+card2)

# 2 - approach-------------------

n= int(input())

values = list(map(int, input().split()))[:n]
values = sorted(values)
left_sum = values[0] * values[1]
right_sum = values[-1] * values[-2]

if left_sum > right_sum:
    print(values[0] + values[1])

else:
    print(values[-1]+values[-2])



# Q - 4-----------------------------------------------------------------------------
# count the perfect square roots
import math

n = int(input())

areas = list(map(int, input().split()))[:n]

# print(type(math.sqrt(81)))
count = 0
for i in areas:
    if i % math.sqrt(i) == 0:
        count += 1
print(count)



