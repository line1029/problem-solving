from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
nums = map(int, stdin.readline().split())
prefix_sum = [0]*n
for idx, num in enumerate(nums):
    # prefix_sum[-1] was 0
    prefix_sum[idx] += prefix_sum[idx-1] + num
intervals = map(lambda x: list(map(lambda y: int(y)-1, x.split())), stdin.readlines())
stdout.write("\n".join(str(prefix_sum[end] - prefix_sum[start - 1]) if start else str(prefix_sum[end]) for start, end in intervals))