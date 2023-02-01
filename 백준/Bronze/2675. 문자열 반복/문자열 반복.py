import sys
t = int(sys.stdin.readline())
arr = [None] * t
for i in range(t):
    n, s = sys.stdin.readline().split()
    arr[i] = "".join([i * int(n) for i in s])
for ans in arr:
    print(ans)
