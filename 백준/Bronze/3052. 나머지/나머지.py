import sys
arr = [False] * 42
for i in range(10):
    arr[int(sys.stdin.readline()) % 42] = True
print(sum(arr))