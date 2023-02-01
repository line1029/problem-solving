import sys
n = int(sys.stdin.readline())
data = [None] * n
for i in range(n):
    data[i] = sum(map(int, sys.stdin.readline().split()))
for idx, num in enumerate(data):
    print(f"Case #{idx + 1}: {num}")