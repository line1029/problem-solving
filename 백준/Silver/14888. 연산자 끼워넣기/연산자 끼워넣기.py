from itertools import permutations
n = int(input())
arr = list(map(int, input().split()))
op = []
for i, j in zip(range(4), list(map(int, input().split()))):
    op += [i]*j
mini = 10**10
maxi = -10**10
for pat in set(permutations(op)):
    val = arr[0]
    for idx, order in enumerate(pat, 1):
        if order == 0:
            val += arr[idx]
        elif order == 1:
            val -= arr[idx]
        elif order == 2:
            val *= arr[idx]
        elif val < 0:
            val = -val
            val //= arr[idx]
            val = -val
        else:
            val //= arr[idx]
    mini = min(mini, val)
    maxi = max(maxi, val)
print(maxi)
print(mini)