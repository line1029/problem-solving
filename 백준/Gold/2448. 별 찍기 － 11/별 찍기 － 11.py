# iterative sol
from sys import stdout
pattern = ["  *  ", " * * ", "*****"]
po = 0
n = int(input())
while not n & 1:
    po += 1
    n //= 2
for i in range(po):
    p1 = (" "*(3*2**i) + x + " "*(3*2**i) for x in pattern)
    p2 = (i + " " + i for i in pattern)
    pattern = [*p1, *p2]
print("\n".join(pattern))