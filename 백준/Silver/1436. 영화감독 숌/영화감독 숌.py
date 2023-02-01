n = int(input())
idx = 0
num = 666
arr = [None] * 10000
while idx < n:
    if "666" in str(num):
        arr[idx] = num
        idx += 1
    num += 1
print(arr[n - 1])