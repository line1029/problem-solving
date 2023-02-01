import sys
m, n = int(sys.stdin.readline()), int(sys.stdin.readline())

s = [True]*(n+1)
s[1] = False
for i in range(2, n+1):
    if s[i]:
        for j in range(2, n//i + 1):
            s[i*j] = False

arr = []
for i in range(m, n+1):
    if s[i]:
        arr.append(i)
if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)