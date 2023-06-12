# Manber-Myers Algorithm
from sys import stdin, stdout
s = stdin.readline().strip()
n = len(s)
suffix_array = list(range(n))
rank_arr = [ord(s[i]) - 97 for i in range(n)]
rank_arr.append(-1)
tmp_arr = [0]*(n + 1)
tmp_arr[-1] = -1
p = 1
while p < n:
    # sort suffix array by given rank
    suffix_array.sort(key=lambda x: (rank_arr[x], rank_arr[min(x + p, n)]))

    # make next rank based on prev rank
    for i in range(n - 1):
        x, y = suffix_array[i], suffix_array[i + 1]
        if rank_arr[x] != rank_arr[y] or rank_arr[x + p] != rank_arr[y + p]:
            tmp_arr[y] = tmp_arr[x] + 1
        else:
            tmp_arr[y] = tmp_arr[x]
    p <<= 1
    rank_arr = tmp_arr[:]
    if rank_arr[suffix_array[n - 1]] == n - 1:
        break

offset = 0
lcp = [0]*n
for i, x in enumerate(rank_arr):
    if x > 0:
        prev = suffix_array[x - 1]
        while max(prev, i) + offset < n and s[prev + offset] == s[i + offset]:
            offset += 1
        lcp[x] = offset
    offset = max(0, offset - 1)
stdout.write(" ".join(map(lambda x: str(x + 1), suffix_array)))
stdout.write("\n")
lcp[0] = "x"
stdout.write(" ".join(map(str, lcp)))