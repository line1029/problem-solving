from sys import stdin
n = int(stdin.readline())
costs = map(lambda x: map(int, x.split()), stdin.read().splitlines())
dp1, dp2, dp3 = [0]*n, [0]*n, [0]*n
dp1[0], dp2[0], dp3[0] = next(costs)
for i, (r, g, b) in enumerate(costs, 1):
    dp1[i] = min(dp2[i-1], dp3[i-1]) + r
    dp2[i] = min(dp1[i-1], dp3[i-1]) + g
    dp3[i] = min(dp2[i-1], dp1[i-1]) + b
print(min(dp1[-1], dp2[-1], dp3[-1]))