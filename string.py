
# ------------------------------------------------------------------------------------------
# string

s = "shiva","kumar","karnati"
m = '-'.join(s)
print(m)



s = "shiva kumar is good person"
print(s.find("shiva"))
print(s.find("bad"))  # if it is not there return -1
print(s.find("person"))  # find it returns the staring insex number




print('shiva123'.isalnum()) # True
print('shiva'.isalnum()) # T
print('a123'.isdigit()) #False
print('shiva123'.isalnum()) #T
print('shiva'.islower()) # T
print(''.islower()) #F
print('SHIVa123'.isupper()) #F
print('SHIVA'.isupper()) #T
print('My Name Is Shiva'.istitle()) #t
print(''.istitle()) #F
print(''.isspace()) #F
print('Hello'.startswith("He")) #T
print('Hello'.endswith("lo")) #T


# -----------------sclicing of string--------------------------------------
name = "shiva"
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])
print(name[0:3])
print(name[2:])
print(name[:4])
print(name[:])
print(name[2:4])
print(name[::-1])
print(name[::-2])

name = "shivakumar"
for i in range(1,len(name)+1):
    print(name[-i],end="")

# -------------------task------reverse string------------------------------
name = "shivakumar"
for i in range((len(name)-1),-1,-1):
    print(name[i],end="")

# -------------------task----------- remove duplicates-------------------------

name = "shivakumar"
newname = ""
for i in name:
    if i not in newname:
        newname += i

print(newname)
