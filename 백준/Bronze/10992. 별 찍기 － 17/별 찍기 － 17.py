n = int(input())
arr = [None]*n
arr[0] = " "*(n - 1) + "*"
arr[-1] = "*"*(2*n - 1)
for i in range(1, n - 1):
    arr[i] = " "*(n - i - 1) + "*" + " "*(2*i - 1) + "*"
print("\n".join(arr))