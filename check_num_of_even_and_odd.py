# check no of even and odd numbers in list

list1 = [2,5,4,8,7,30,45,23,57,68]      #------>O(1)
e = 0
o = 0
for i in list1:                #------>O(n)
    if i%2 == 0:               #-------> O(1)
        e += 1                 #------->O(1)
    else:
        o += 1                 #--------> O(1)

print("even = ",e)              #--------> O(1)
print("odd = ",o)               #--------> O(1)


#--------->>>>>> TOTAL TIME COMPLEXITY  =>  O(1)+O(n) = O(n) <<<<<<<<---------

