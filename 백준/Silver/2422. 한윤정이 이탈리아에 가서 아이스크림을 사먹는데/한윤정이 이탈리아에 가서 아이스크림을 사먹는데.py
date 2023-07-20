from sys import stdin
from itertools import combinations
def main():
    n, m = map(int, stdin.readline().split())
    graph = [0]*(n + 1)
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a] |= (1 << b)
        graph[b] |= (1 << a)
    ans = 0
    for a, b, c in combinations(range(1, n + 1), 3):
        if (1 << a)&(graph[b]|graph[c]) or (1 << b)&graph[c]: continue
        ans += 1
    print(ans)
main()