import sys
l = []
n = int(sys.stdin.readline())
for i in range(n):
    l.append(sys.stdin.readline())
l = sorted(list(map(int, l)))
for i in l:
    print(i)