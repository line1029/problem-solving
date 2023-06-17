n = int(input())
M = 1_000_000_000
bitdp = [[[0]*1024 for _ in range(10)] for _ in range(n)]
for i in range(1, 10):
    bitdp[0][i][1 << i] = 1
for i in range(1, n):
    for j in range(10):
        for k in range(1024):
            if j == 0:
                bitdp[i][j][k|(1 << j)] += bitdp[i - 1][j + 1][k]
            elif j == 9:
                bitdp[i][j][k|(1 << j)] += bitdp[i - 1][j - 1][k]
            else:
                bitdp[i][j][k|(1 << j)] += bitdp[i - 1][j - 1][k] + bitdp[i - 1][j + 1][k]
            bitdp[i][j][k|(1 << j)] %= M
print(sum(bitdp[-1][j][1023] for j in range(10))%M)