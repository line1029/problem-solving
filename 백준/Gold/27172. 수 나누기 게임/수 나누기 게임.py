import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input())
arr = list(map(int, input().split()))
x = max(arr) + 1
s = {v:i for i, v in enumerate(arr)}
ans = [0]*n
for i in arr:
    for j in range(2*i, x, i):
        if j in s:
            ans[s[i]] += 1
            ans[s[j]] -= 1

print(" ".join(map(str, ans)))