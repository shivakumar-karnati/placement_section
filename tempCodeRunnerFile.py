
import math

n = int(input())

areas = list(map(int, input().split()))[:n]

# print(type(math.sqrt(81)))
count = 0
for i in areas:
    if i % math.sqrt(i) == 0:
        count += 1
print(count)