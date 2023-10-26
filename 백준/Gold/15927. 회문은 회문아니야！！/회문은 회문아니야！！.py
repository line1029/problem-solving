from sys import stdin
s = stdin.readline().strip()
if s != s[::-1]:
    print(len(s))
elif s[:-1] != s[-2::-1]:
    print(len(s) - 1)
else:
    print(-1)