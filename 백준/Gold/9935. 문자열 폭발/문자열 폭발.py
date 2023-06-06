from sys import stdin
s = stdin.readline().rstrip()
bomb = stdin.readline().rstrip()
n = len(bomb) - 1
stack = []
for char in s:
    if char == bomb[-1] and len(stack) >= n:
        for i, j in zip(bomb, stack[len(stack) - n:]):
            if i != j:
                break
        else:
            for _ in range(n):
                stack.pop()
            continue
    stack.append(char)
if stack:
    print("".join(stack))
else:
    print("FRULA")