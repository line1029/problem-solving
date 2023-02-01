import sys
n = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
m = max(scores)
print(sum(scores) / n / m * 100)
