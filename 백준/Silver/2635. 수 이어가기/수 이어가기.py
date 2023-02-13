n = int(input())

_max = 0
for i in range(1, n + 1):
    seq = [n, i, n - i]
    while seq[-1] <= seq[-2]:
        seq.append(seq[-2] - seq[-1])
    if len(seq) > _max:
        ans = seq
        _max = len(seq)

print(_max)
print(" ".join(map(str, ans)))