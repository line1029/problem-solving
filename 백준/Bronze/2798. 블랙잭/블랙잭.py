from sys import stdin
n, m = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
cards.sort(reverse=True)
ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                ans = max(ans, total)
                break
print(ans)