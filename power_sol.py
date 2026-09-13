#--------> power solution------------------------------------------------------------------->

def power(base,exponent):
    if exponent == 0:
        return 1
    return base * power(base,exponent-1)

base = int(input("Enter base number :"))
exponent = int(input("Enter exponenet number :"))

print(power(base,exponent))
