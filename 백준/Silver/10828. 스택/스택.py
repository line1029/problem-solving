from sys import stdin, stdout
from collections import deque
n = int(stdin.readline())
queries = stdin.readlines()
def stack_action(stack, query):
    if query == "top\n":
        if stack:
            return stack[-1]
        return -1
    if query == "pop\n":
        if stack:
            return stack.pop()
        return -1
    if query == "size\n":
        return len(stack)
    if query == "empty\n":
        return int(len(stack) == 0)
    stack.append(int(query.split()[1]))

stack = deque()
for query in queries:
    ans = stack_action(stack, query)
    if ans is not None:
        stdout.write(f"{ans}\n")