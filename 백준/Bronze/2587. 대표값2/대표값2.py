import sys
arr = [0]*5
for i in range(5):
    arr[i] += int(sys.stdin.readline())
arr.sort()
print(sum(arr)//5)
print(arr[2])