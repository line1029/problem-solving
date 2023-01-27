from sys import stdin
sentences = stdin.readlines()
sentences.pop()
closes = {")":"(", "]":"["}
opens = {"(", "["}
def is_valid(s):
    stack = []
    for char in s:
        if char in opens:
            stack.append(char)
        elif char in closes:
            if stack and stack[-1] == closes[char]:
                stack.pop()
            else:
                return False
    return not stack

for s in sentences:
    if is_valid(s):
        print("yes")
    else:
        print("no")