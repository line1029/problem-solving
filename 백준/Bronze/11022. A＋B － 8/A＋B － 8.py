import sys
n = int(sys.stdin.readline())
data = [None] * n
for i in range(n):
    data[i] = list(map(int, sys.stdin.readline().split()))
for idx, nums in enumerate(data):
    print(f"Case #{idx + 1}: {nums[0]} + {nums[1]} = {sum(nums)}")