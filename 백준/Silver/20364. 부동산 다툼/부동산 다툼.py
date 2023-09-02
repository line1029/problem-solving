import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, q = map(int, input().split())
tree = [0]*(n + 1)
ans = __pypy__.builders.StringBuilder()
for _ in range(q):
    i = wanted = int(input())
    x = 0
    while i:
        if tree[i]:
            x = i
        i >>= 1
    if x:
        ans.append(f"{x}\n")
    else:
        ans.append("0\n")
        tree[wanted] = 1
os.write(1, ans.build().encode())