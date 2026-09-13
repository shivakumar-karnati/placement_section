# -----------task 1  ------------------------------------------------------------------
# move zeros in list to the last

list2 = [2,4,6,7,0,4,6,0,7]
print(list2)
for i in list2:
    if i == 0:
        list2.remove(i)
        list2.append(i)
print(list2)

#---- total time complexity  -> O(n)

# ----task 2 ---find max and min in list-------------------------------------------------------

list3 = [4,6,45,7,8,9,2]

print(max(list3))   #--------time complexity ->O(1)
print(min(list3))

mx = list3[0]
mn = list3[0]
for i in list3:
    if i >mx:
        mx = i
    if i < mn:
        mn = i
print(mx)
print(mn)
#------ time complexity -> O(n)



#---task 3 ----- second highest number--------------------------------------------------------

list4 = [2,4,5,6,34,5,6,37,35]
la=sl = list4[0]
for i in list4:
    if i>la:
        sl = la
        la = i
    elif i > sl and i != la:
        sl = i

print(sl)

#-----time complexity -> O(n)
list4.sort()
print(list4[-2])
#--- time complexity -> O(1)


#-----task-4 ------------------------------------------------------------------------
# product of all the elements except itself

l5 = [1,2,3,4]
p=1
ex = []
for i in range(len(l5)):    #----time complexity ->O(n)
    for j in l5:           #-----time cpmplexity -.O(n)
        p = p*j
    p = p//l5[i]
    ex.append(p)
    p = 1

print(ex)  
#-------total time complexity  O(n)*O(n) = O(n^2)

#---------------task-5-------------------------------------------------------------------------------
# --count the highest consecutive 1s in binary numbers ------>

def count_consicutive(s):
    count = 0
    maxcount = 0
    for i in s:
        if i == 1:
            count += 1
            maxcount = max(maxcount,count)
        else:
            count = 0
    return maxcount


s = [1,1,0,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1]
print(count_consicutive(s))


#----- task - 6 --------------------------------------------------------------------------------
#----------------taks------------------------check palindrome
# check with loop

def palindrome(s):
    for i in range(len(s)):
        if s[i] == s[len(s)-1-i]:
            return "palindrome"
        else:
            return "Not palindrome"

s = input()
print(palindrome(s))


#--------- task-7------------------------------------------------------------------------------------
#-------------------taks----------count vowel and consonants---------

def counts(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    vc = 0
    c = 0
    for i in s:
        if i in vowels:
            vc += 1
        else:
            c += 1
    print(vc,c)
            

s = input()
counts(s)

#-------------task-8 ---------------------------------------------------------------------
#-------task -------------- check anagram---

def anagram(s1,s2):
    if len(s1) == len(s2):
        s1 = "".join(sorted(s1))
        s2 ="".join(sorted(s2))
        if s1[:] == s2[:]:
            return "anagram"
        else:
            return "not anagram"
    else:
        return "not anagram"

s1 = input()
s2 = input()
print(anagram(s1,s2))

#----------- task-9-------------------------------------------------------------------------------
#-------------task----count words in sentence----------

var =" this is a sentence  "
var1 = var.strip()
count = 1
for i in var:
    if i == " ":
        count +=1
print(count)
# -----------------------
var =" this is a sentence  "
var1 = var.split()
print(len(var1))

#--------- taskk- 10-----------------------------------------------------------------------------------
#-------------task -----------count special charecter in a message----------------------------------

m = input()
wh = 0
sp = 0

for i in m:
    if i == " ":
        wh += 1
    a = ord(i)
    if (a >=33 and a<=47) or (a>=58 and a<=64) or (a>=91 and a<=96) or (a>=123 and a<=126):
        sp += 1

print(wh)
print(sp)


#-------task ---------- title case a sentence--------------------------------

t = input()
print(t.title())




#------->>>>>>>>>>>>>>>>>>>task----------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....

s = input("Enter something")
star = ""
w= ""
for i in s:
    if i == "*":
        star += i
    else:
        w += i
print(star+w)

# -------------->>>>>>>>>>>>>>>>>>>>>>> task  -------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>.

s = input("enter something :")
s = list(s)
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count +=1
    else:
        print(f"{s[i]}{count}",end="")
        count = 1
if count > 1:
    print(f"{s[i]}{count}")
else:
    print(f"{s[-1]}1")
    

#--------------------------------->>>>>>Task>>>>>>>>>>>>>>>...---------------------------------------

employees = int(input("Enter the No of Employees :"))

r1,r2 = list(map(int, input("Enter the range :").split()))

distances = list(map(int, input("Enter the Distance of a Employees :").split()))[:employees]
inDistance =[]
for i in distances:
    if r1 <= i <= r2:
        inDistance.append(i)

print(inDistance)







