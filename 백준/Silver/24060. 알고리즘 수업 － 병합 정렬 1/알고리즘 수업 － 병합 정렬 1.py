ans = []
def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q+1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    i, j, t = p, q+1, 0
    tmp = [None] * (r - p + 1)
    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp[t] = arr[i]
            i += 1
        else:
            tmp[t] = arr[j]
            j += 1
        t += 1
    while i <= q:
        tmp[t] = arr[i]
        i += 1
        t += 1
    while j <= r:
        tmp[t] = arr[j]
        j += 1
        t += 1
    i = p
    t = 0
    while i <= r:
        arr[i] = tmp[t]
        i += 1
        t += 1
    ans.extend(tmp)

from sys import stdin, stdout
n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
merge_sort(arr, 0, len(arr)-1)
if k <= len(ans):
    print(ans[k-1])
else:
    print(-1)