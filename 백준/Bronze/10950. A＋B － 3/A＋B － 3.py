import sys
n = int(input())
data = [None] * n
for i in range(n):
    data[i] = str(sum(map(int, sys.stdin.readline().split())))
print("\n".join(data))
