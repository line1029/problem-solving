from sys import stdin
from functools import cmp_to_key

n = int(stdin.readline())
stack = [list(map(int, stdin.readline().split()))]
points = []
for _ in range(n - 1):
    nex = list(map(int, stdin.readline().split()))
    if stack[0][1] > nex[1] or stack[0][1] == nex[1] and stack[0][0] > nex[0]:
        points.append(stack.pop())
        stack.append(nex)
    else:
        points.append(nex)
a = stack[0]
def cmp(b, c):
    res = (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])
    if res:
        return -res
    if b[1] != c[1]:
        return b[1] - c[1]
    return b[0] - c[0]
def ccw(x, y, z):
    return (y[0] - x[0])*(z[1] - x[1]) - (y[1] - x[1])*(z[0] - x[0])
points.sort(key=cmp_to_key(cmp))
for i in range(n - 1):
    while len(stack) >= 2 and ccw(stack[-2], stack[-1], points[i]) <= 0:
        stack.pop()
    stack.append(points[i])
print(len(stack))