from sys import stdin
from itertools import permutations
input = stdin.readline
n = int(input())
arr = list(map(int, input().split()))
_max = 0
def get_diff_sum(arr):
    res = 0
    for i in range(1, n):
        res += abs(arr[i - 1] - arr[i])
    return res
for cand in permutations(arr):
    _max = max(_max, get_diff_sum(cand))
print(_max)