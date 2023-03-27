from sys import stdin
from itertools import islice
s = stdin.readline()
ans = 0
stack = 1
for idx, char in enumerate(islice(s, 1, len(s) - 1), 1):
    if char == ")":
        stack -= 1
        if s[idx - 1] == "(":
            ans += stack
        else:
            ans += 1
    else:
        stack += 1
print(ans)