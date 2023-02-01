import math
d = input().split()
a = int(d[0])
b = int(d[1])
v = int(d[2])
if a <= v:
    n = math.ceil(((v - a) / (a - b)) + 1)
else:
    n = 1
print(n)