a, b = input().split()
if len(a) < len(b): a, b = b, a
b = "0"*(len(a) - len(b)) + b
for i in range(len(a)):
    print(int(a[i]) + int(b[i]), end="")