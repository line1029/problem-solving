from sys import stdin
def main():
    n, m = map(int, stdin.readline().split())
    if n <= m:
        print(n)
        exit()
    n -= m
    rides = list(map(int, stdin.readline().split()))
    arr = [0]*31
    for i in rides:
        arr[i] += 1
    lo, hi = 1, 30*(n + m)
    while lo < hi:
        mid = (lo + hi) >> 1
        if sum((mid//i)*arr[i] for i in range(1, 31)) >= n:
            hi = mid
        else:
            lo = mid + 1
    done = sum((lo//i)*arr[i] for i in range(1, 31))
    for i in range(m - 1, -1, -1):
        if not lo%rides[i]:
            if done == n:
                print(i + 1)
                exit()
            done -= 1
main()