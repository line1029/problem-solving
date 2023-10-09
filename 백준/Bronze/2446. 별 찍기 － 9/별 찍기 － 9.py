n = int(input())
arr = [None]*(2*n - 1)
for i in range(n):
    arr[i] = arr[- i - 1] = " "*i + "*"*(2*n - 2*i - 1)
print("\n".join(arr))