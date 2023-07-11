import os, io, __pypy__
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, m, k = map(int, input().split())
cards = sorted(map(int, input().split()))
parents = list(range(n + 1))
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parents[y] = x

def bsr(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) >> 1
        if x < find(a[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo
ans = __pypy__.builders.StringBuilder()
for x in map(int, input().split()):
    i = bsr(cards, x)
    union(cards[i - 1] if i else 0, cards[i])
    ans.append(f"{cards[i]}\n")
os.write(1, ans.build().encode())