num = 123456
rev = 0
while num>0:
    last = num % 10
    rev = rev*10 +last
    num = num //10

print(rev)
