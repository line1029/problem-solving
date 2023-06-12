from sys import stdin
n, m = map(int, stdin.readline().split())
nums = [0] * (n + 1)
intervals = [0] * m
for i, num in enumerate(map(int, stdin.readline().split()), 1):
    nums[i] = (nums[i - 1] + num) % m
    intervals[nums[i]] += 1
intervals[0] += 1
ans = 0
for i in intervals:
    ans += i*(i-1)//2
print(ans)