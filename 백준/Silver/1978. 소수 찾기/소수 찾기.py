s = [True]*1001
s[1] = False
for i in range(2, 1001):
    if s[i]:
        for j in range(2, 1000//i + 1):
            s[i*j] = False
import sys
n = int(sys.stdin.readline())
nums = map(int, sys.stdin.readline().split())
print(sum((s[i] for i in nums)))