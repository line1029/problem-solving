from sys import stdin
stdin.readline()
stack = []
for num in map(int, stdin.read().splitlines()):
    while stack and stack[-1] <= num:
        stack.pop()
    stack.append(num)
print(len(stack))