import sys
cur = n = int(sys.stdin.readline())
idx = 0
while idx == 0 or cur != n:
    cur = (cur % 10) * 10 + (cur // 10 + cur % 10) % 10
    idx += 1
print(idx)