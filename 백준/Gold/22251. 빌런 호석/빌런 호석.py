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
n, k, p, x = map(int, input().split())
ans = -1
for i in range(1, n + 1):
    needed_invert = 0
    q1, q2 = x, i
    for _ in range(k):
        q1, r1 = divmod(q1, 10)
        q2, r2 = divmod(q2, 10)
        needed_invert += INVERT_MAP[r1][r2]
        if not q1 and not q2:
            break
    if needed_invert <= p:
        ans += 1
print(ans)