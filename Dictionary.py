
#----->>>Dictionary-------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

stu = {
    101:"shiva",
    102:"kumar",
    "101":"karnati",
    101:"bunny",
    "name":"shiva"
}
# print(stu)

for i in stu:
    print(i)


for i in stu.keys():
    print(i)


for i in stu.values():
    print(i)


for i in stu.items():
    print(i)


stu.pop(101)
print(stu)


stu.clear()
print(stu)


newstu = stu.copy()
print(stu)
print(newstu)


print(stu[102])


stu['color'] = 'black'
print(stu)
