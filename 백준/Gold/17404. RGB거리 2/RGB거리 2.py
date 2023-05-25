# RGB
from sys import stdin
from itertools import islice
n = int(stdin.readline())
dp = [[1000001]*n for _ in range(9)]
prices = map(lambda x: list(map(int, x.split())), stdin.read().splitlines())
rgb0 = next(prices)
rgb1 = next(prices)
for start_rgb_idx in range(3):
    for cur_rgb_idx in range(3):
        if start_rgb_idx != cur_rgb_idx:
            dp[start_rgb_idx*3 + cur_rgb_idx][1] = rgb0[start_rgb_idx] + rgb1[cur_rgb_idx]
for idx, rgb in enumerate(islice(prices, n-2), 2):
    for start_rgb_idx in range(3):
        for cur_rgb_idx in range(3):
            dp[start_rgb_idx*3 + cur_rgb_idx][idx] = min(
                dp[start_rgb_idx*3 + (cur_rgb_idx + 1)%3][idx-1],
                dp[start_rgb_idx*3 + (cur_rgb_idx + 2)%3][idx-1]
            ) + rgb[cur_rgb_idx]
print(min(dp[i][n-1] for i in range(9) if i%3 != (i//3)%3))