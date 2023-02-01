import sys
n, x = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b, idx, ptr = [None] * n, 0, 0
while idx < n:
    if a[idx] < x:
        b[ptr] = a[idx]
        ptr += 1
    idx += 1
print(" ".join(map(str, b[:ptr])))
