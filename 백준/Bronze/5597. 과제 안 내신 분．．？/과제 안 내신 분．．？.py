import sys
s = set(range(1, 31))
for _ in range(28):
    s.discard(int(sys.stdin.readline()))
l = sorted(list(s))
for i in l:
    print(i)