# iterative sol
def iterative(s):
    arr = []
    idx = 0
    stack = []
    for i, char in enumerate(s):
        if char == ")":
            if idx < i:
                arr.append(i - idx)
            arr.append(s[i])
            idx = i + 1
        elif char == "(":
            if idx < i - 1:
                arr.append(i - 1 - idx)
            arr.append(int(s[i - 1]))
            arr.append(s[i])
            idx = i + 1
    if idx != len(s):
        arr.append(len(s) - idx)
    for i in arr:
        if i == ")":
            x = []
            while stack[-1] != "(":
                x.append(stack.pop())
            stack.pop()
            stack.append(sum(x)*stack.pop())
        else:
            stack.append(i)
    return sum(stack)
print(iterative(input()))
