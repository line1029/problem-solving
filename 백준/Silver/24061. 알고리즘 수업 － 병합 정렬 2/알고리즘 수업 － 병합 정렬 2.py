from sys import stdin, stdout

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
log2 = -1
m = n
while m:
    m >>= 1
    log2 += 1
if n * log2 + ((n - (1 << log2)) << 1) < k:
    stdout.write("-1")
    exit()
step = [0]


def merge_sort(array, p, r):
    if p < r:
        q = (p + r) >> 1
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)


def merge(array, p, q, r):
    i, j, t = p, q + 1, 0
    tmp = [0] * (r - p + 1)
    while i <= q and j <= r:
        if array[i] <= array[j]:
            tmp[t] = array[i]
            i += 1
        else:
            tmp[t] = array[j]
            j += 1
        t += 1
    while i <= q:
        tmp[t] = array[i]
        i += 1
        t += 1
    while j <= r:
        tmp[t] = array[j]
        j += 1
        t += 1
    for i in range(r - p + 1):
        array[p + i] = tmp[i]
        step[0] += 1
        if step[0] == k:
            stdout.write(" ".join(map(str, array)))
            exit()


merge_sort(arr, 0, n - 1)
