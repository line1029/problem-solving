from sys import stdin
from collections import deque
gears = [deque(stdin.readline().strip()) for _ in range(4)]
k = int(stdin.readline())
for i, ori in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    i -= 1
    stack = [i]
    act = [i]
    while stack:
        cur = stack.pop()
        if cur - 1 >= 0 and cur - 1 not in act and gears[cur][6] != gears[cur - 1][2]:
            act.append(cur - 1)
            stack.append(cur - 1)
        if cur + 1 < 4 and cur + 1 not in act and gears[cur][2] != gears[cur + 1][6]:
            act.append(cur + 1)
            stack.append(cur + 1)
    for x in act:
        if (i - x)&1:
            gears[x].rotate(-ori)
        else:
            gears[x].rotate(ori)
print(sum(2**i * (gears[i][0] == "1") for i in range(4)))