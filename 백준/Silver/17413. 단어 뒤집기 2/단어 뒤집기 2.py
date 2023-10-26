from sys import stdin
ans = []
stack = []
tag = False
for char in stdin.readline().strip():
    if char == "<":
        tag = True
        if stack:
            ans.append("".join(reversed(stack)))
            stack.clear()
        stack.append(char)
    elif char == ">":
        tag = False
        stack.append(char)
        ans.append("".join(stack))
        stack.clear()
    elif char == " " and not tag:
        if stack:
            ans.append("".join(reversed(stack)))
            stack.clear()
        ans.append(" ")
    else:
        stack.append(char)
if stack:
    ans.append("".join(reversed(stack)))
print("".join(ans))