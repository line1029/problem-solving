from sys import stdin
n, k = map(int, stdin.readline().split())
arr = list(map(lambda x: int(x)&1, stdin.readline().split()))
odds = [0]*k
evens = [0]*k
dp_odds = [0]*k
dp_evens = [0]*k
for i, v in enumerate(arr):
    i %= k
    if v:
        odds[i] += 1
    else:
        evens[i] += 1
dp_evens[0] = odds[0]
dp_odds[0] = evens[0]
for i in range(1, k):
    dp_odds[i] = min(dp_evens[i - 1] + evens[i], dp_odds[i - 1] + odds[i])
    dp_evens[i] = min(dp_evens[i - 1] + odds[i], dp_odds[i - 1] + evens[i])
print(dp_evens[-1])