from bisect import bisect_left

def get_count_from_time(officers, given_time):
    return sum(given_time // i for i in officers)

def solution(n, times):
    lo, hi = 1, n * min(times)
    while lo < hi:
        mid = (lo + hi) >> 1
        if get_count_from_time(times, mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo