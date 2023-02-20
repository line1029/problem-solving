import sys
s = sys.stdin.readline().strip()
stack1 = [i for i in s]
stack2 = []


m = int(sys.stdin.readline())
for i in range(m):
    process = sys.stdin.readline().strip()
    if process[0] == "L" and stack1:
        stack2.append(stack1.pop())
    elif process[0] == "D" and stack2:
        stack1.append(stack2.pop())
    elif process[0] == "B" and stack1:
        stack1.pop()
    elif process[0] == "P":
        stack1.append(process[2])

res = "".join(stack1) + "".join(stack2[::-1])
print(res)