from sys import stdin
from collections import deque


def main():
    s = stdin.readline()
    n = len(s)
    if s[-1] == "\n":
        n -= 1
    a = deque(filter(lambda x: s[x] == "A", range(n)))
    b = deque(filter(lambda x: s[x] == "B", range(n)))
    c = deque(filter(lambda x: s[x] == "C", range(n)))
    ans = 0
    for idx_c in c:
        if not b or b[0] > idx_c:
            continue
        b.popleft()
        ans += 1
    for idx_a in reversed(a):
        if not b or b[-1] < idx_a:
            continue
        b.pop()
        ans += 1

    print(ans)


main()
