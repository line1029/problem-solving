from sys import stdin
bracket = stdin.readline().rstrip()
closes = {"]":"[", ")":"("}
def is_valid(s):
    stack = []
    for char in s:
        if char not in closes:
            stack.append(char)
        elif stack and stack[-1] == closes[char]:
            stack.pop()
        else:
            return False
    return not stack

if not is_valid(bracket):
    print(0)
    exit()

def recur(s):
    if not s:
        return 1
    if s == "[]":
        return 3
    if s == "()":
        return 2
    partition = []
    stack = []
    for idx, char in enumerate(s):
        if char not in closes:
            stack.append(char)
        else:
            stack.pop()
        if not stack:
            partition.append(idx + 1)
    res = [s[0:partition[0]]]
    for i in range(1, len(partition)):
        res.append(s[partition[i - 1]:partition[i]])
    return sum(3*recur(i[1:-1]) if i[0] == "[" else 2*recur(i[1:-1]) for i in res)

print(recur(bracket))