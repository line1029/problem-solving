from sys import stdin
n = int(stdin.readline())
arr = map(int, stdin.readline().split())
b, c = map(int, stdin.readline().split())
ans = 0
for need in arr:
    need = max(0, need - b)
    ans += need//c + (need%c != 0) + 1
print(ans)