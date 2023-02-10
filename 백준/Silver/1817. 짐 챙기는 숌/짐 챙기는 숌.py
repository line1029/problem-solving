from sys import stdin
n, m = map(int, stdin.readline().split())
if not n:
    print(0)
    exit()
books = map(int, stdin.readline().split())
cur = 0
ans = 0
for book in books:
    if cur + book > m:
        cur = 0
        ans += 1
    cur += book
if cur:
    ans += 1
print(ans)