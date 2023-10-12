from sys import stdin
for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    books = [0]*(n + 1)
    ans = 0
    wanted = sorted(map(lambda x: list(map(int, x.split())), (stdin.readline() for __ in range(m))), key=lambda x: (x[1], -x[0]))
    for i, j in wanted:
        for k in range(i, j + 1):
            if not books[k]:
                books[k] = 1
                ans += 1
                break
    print(ans)