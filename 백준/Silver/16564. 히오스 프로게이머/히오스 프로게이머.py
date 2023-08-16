import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def main():
    n, k = map(int, input().split())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())
    arr.sort()
    lo, hi = 0, 2_000_000_000
    while lo < hi:
        mid = (lo + hi + 1) >> 1
        flag = True
        tmp_k = k
        for i in range(n):
            if arr[i] > mid: break
            tmp_k -= (mid - arr[i])
            if tmp_k < 0:
                flag = False
                break
        if flag:
            lo = mid
        else:
            hi = mid - 1
    print(lo)
main()