from sys import stdin
from bisect import bisect
def main():
    n = int(stdin.readline())
    papers = []
    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        if a > b:
            a, b = b, a
        papers.append((a, b))
    papers.sort()
    dp = []
    for _, i in papers:
        k = bisect(dp, i)
        if k == len(dp):
            dp.append(i)
        else:
            dp[k] = i
    print(len(dp))
    
main()