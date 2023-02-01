import sys
m, idx = 0, 0
for i in range(1, 10):
    num = int(sys.stdin.readline())
    if num > m:
        m = num
        idx = i
print(m)
print(idx)