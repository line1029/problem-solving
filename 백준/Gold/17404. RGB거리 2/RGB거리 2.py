# RGB
from sys import stdin
from itertools import islice
n = int(stdin.readline())
dp = [[0]*n for _ in range(9)]
prices = map(lambda x: list(map(int, x.split())), stdin.read().splitlines())
dp[0][0], dp[4][0], dp[8][0] = next(prices)
r1, g1, b1 = next(prices)
dp[1][1], dp[2][1] = dp[0][0] + g1, dp[0][0] + b1
dp[3][1], dp[5][1] = dp[4][0] + r1, dp[4][0] + b1
dp[6][1], dp[7][1] = dp[8][0] + r1, dp[8][0] + g1
if n == 2:
    print(min(dp[i][1] for i in range(9) if dp[i][1]))
    exit()
r2, g2, b2 = next(prices)
if n == 3:
    print(min(
        dp[1][1] + b2, dp[2][1] + g2, dp[3][1] + b2, dp[5][1] + r2, dp[6][1] + g2, dp[7][1] + r2
    ))
    exit()
dp[0][2], dp[1][2], dp[2][2] = min(dp[1][1], dp[2][1]) + r2, dp[2][1] + g2, dp[1][1] + b2
dp[3][2], dp[4][2], dp[5][2] = dp[5][1] + r2, min(dp[5][1], dp[3][1]) + g2, dp[3][1] + b2
dp[6][2], dp[7][2], dp[8][2] = dp[7][1] + r2, dp[6][1] + g2, min(dp[6][1], dp[7][1]) + b2

for idx, rgb in enumerate(islice(prices, n-4), 3):
    for start_rgb_idx in range(3):
        for cur_rgb_idx in range(3):
            dp[start_rgb_idx*3 + cur_rgb_idx][idx] = min(
                dp[start_rgb_idx*3 + (cur_rgb_idx + 1)%3][idx-1],
                dp[start_rgb_idx*3 + (cur_rgb_idx + 2)%3][idx-1]
            ) + rgb[cur_rgb_idx]

rn, gn, bn = next(prices)
dp[1][n-1] = min(dp[0][n-2], dp[2][n-2]) + gn
dp[2][n-1] = min(dp[0][n-2], dp[1][n-2]) + bn
dp[3][n-1] = min(dp[4][n-2], dp[5][n-2]) + rn
dp[5][n-1] = min(dp[3][n-2], dp[4][n-2]) + bn
dp[6][n-1] = min(dp[7][n-2], dp[8][n-2]) + rn
dp[7][n-1] = min(dp[6][n-2], dp[8][n-2]) + gn
print(min(dp[i][n-1] for i in range(9) if dp[i][n-1]))
