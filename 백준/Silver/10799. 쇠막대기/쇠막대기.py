from sys import stdin
s = stdin.readline()
ans = 0
stack = 0
for idx, char in enumerate(s):
    if char == ")":
        stack -= 1
        if s[idx - 1] == "(":
            ans += stack
        else:
            ans += 1
    else:
        stack += 1
print(ans)