INVERT_MAP = [
    [0, 4, 3, 3, 4, 3, 2, 3, 1, 2],
    [4, 0, 5, 3, 2, 5, 6, 1, 5, 4],
    [3, 5, 0, 2, 5, 4, 3, 4, 2, 3],
    [3, 3, 2, 0, 3, 2, 3, 2, 2, 1],
    [4, 2, 5, 3, 0, 3, 4, 3, 3, 2],
    [3, 5, 4, 2, 3, 0, 1, 4, 2, 1],
    [2, 6, 3, 3, 4, 1, 0, 5, 1, 2],
    [3, 1, 4, 2, 3, 4, 5, 0, 4, 3],
    [1, 5, 2, 2, 3, 2, 1, 4, 0, 1],
    [2, 4, 3, 1, 2, 1, 2, 3, 1, 0]
]
from sys import stdin
n, k, p, x = map(int, stdin.readline().split())
ans = -1
x = list(map(int, (k - len(str(x)))*"0" + str(x)))[::-1]
goal = [0] * k
for _ in range(n):
    digit_idx = 0
    digit_sum = goal[digit_idx] + 1
    carry, digit= divmod(digit_sum, 10)
    goal[digit_idx] = digit
    while carry:
        digit_idx += 1
        digit_sum = goal[digit_idx] + carry
        carry, digit= divmod(digit_sum, 10)
        goal[digit_idx] = digit
    needed_invert = sum(INVERT_MAP[i][j] for i, j in zip(goal, x))
    if needed_invert <= p:
        ans += 1
print(ans)
