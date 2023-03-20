import sys
from itertools import product
input = sys.stdin.readline
n, m = map(int, input().split())
nums = sorted(input().split(), key=lambda x: int(x))
ans = nums[:]
for _ in range(m - 1):
    tmp = []
    for i, j in product(ans, nums):
        tmp.append(i + " " + j)
    ans = tmp
print("\n".join(ans))