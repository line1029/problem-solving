import sys
n = int(sys.stdin.readline())
data = [None] * n
for i in range(n):
    data[i] = str(sum(map(int, sys.stdin.readline().split())))

print("\n".join(data))
