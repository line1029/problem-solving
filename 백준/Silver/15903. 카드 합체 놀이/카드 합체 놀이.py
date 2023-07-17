from sys import stdin
from heapq import *
def main():
    n, m = map(int, stdin.readline().split())
    cards = list(map(int, stdin.readline().split()))
    heapify(cards)
    for _ in range(m):
        a, b = heappop(cards), heappop(cards)
        heappush(cards, a + b)
        heappush(cards, a + b)
    print(sum(cards))
main()