import sys
n = int(sys.stdin.readline())
s = set()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(10):
        for j in range(10):
            s.add((x+i, y+j))

print(len(s))