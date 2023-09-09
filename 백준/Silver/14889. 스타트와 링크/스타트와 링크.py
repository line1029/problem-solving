from sys import stdin
from itertools import combinations
input = stdin.readline
def main():
    n = int(input())
    grid = [0]*n
    for i in range(n):
        grid[i] = list(map(int, input().split()))
    ans = sum(map(sum, grid))
    for pat in combinations(range(n), n//2):
        stat_link = stat_start = 0
        pat_start = [i for i in range(n) if i not in pat]
        for i in range(n//2):
            for j in range(i + 1, n//2):
                stat_link += grid[pat[i]][pat[j]] + grid[pat[j]][pat[i]]
                stat_start += grid[pat_start[i]][pat_start[j]] + grid[pat_start[j]][pat_start[i]]
        ans = min(ans, abs(stat_start - stat_link))
    print(ans)
main()