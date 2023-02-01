import sys
n = int(sys.stdin.readline())
data = "\n".join(map(str, (i for i in range(n, 0, -1))))
print(data)