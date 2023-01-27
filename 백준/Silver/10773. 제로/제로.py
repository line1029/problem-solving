from sys import stdin
k = int(stdin.readline())
nums = list(map(int, stdin.readlines()))
stack = []
for num in nums:
    if not num:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))