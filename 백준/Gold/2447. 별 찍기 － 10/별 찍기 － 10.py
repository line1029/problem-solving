pattern = ["***", "* *", "***"]
n = int(input())
po = -1
while n:
    po += 1
    n //= 3
for i in range(1, po):
    p1 = [j*3 for j in pattern]
    p2 = [j+" "*3**i+j for j in pattern]
    pattern = [*p1, *p2, *p1]
print("\n".join(pattern))