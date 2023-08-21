import io,os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    n, k = map(int, input().split())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())
    arr.sort()
    lo, hi = 0, arr[-1] + k
    while lo < hi:
        mid = (lo + hi + 1) >> 1
        tmp_k = k
        for i in range(n):
            if arr[i] > mid:
                lo = mid
                break
            tmp_k -= (mid - arr[i])
            if tmp_k < 0:
                hi = mid - 1
                break
        else:
            lo = mid
    print(lo)
main()