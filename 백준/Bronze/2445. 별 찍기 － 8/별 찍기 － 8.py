a = []
n = int(input())
for i in range(1, n + 1):
    a.append("*"*i + " "*(2*(n - i)) + "*"*i)
    print(a[-1])
for i in range(-2, -n - 1, -1):
    print(a[i])