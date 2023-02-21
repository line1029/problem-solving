# iterative sol
from sys import stdout
pattern = ["  *  ", " * * ", "*****"]
po = 0
n = int(input())
while not n & 1:
    po += 1
    n //= 2
for i in range(po):
    p1 = ("".join([" "*(3*2**i), x, " "*(3*2**i)]) for x in pattern)
    p2 = (" ".join(x) for x in zip(pattern, pattern))
    pattern = [*p1, *p2]
stdout.writelines(f"{p}\n" for p in pattern)