from sys import stdin, stdout

res = []
for _ in range(int(stdin.readline())):
    applies = sorted(
        map(lambda x: list(map(int, x.split())), (stdin.readline() for __ in range(int(stdin.readline()))))
    )
    cur = applies[0][1]
    ans = 1
    for i, j in applies:
        if j < cur:
            ans += 1
            cur = j
        if cur == 1: break
    res.append(ans)
stdout.write("\n".join(map(str, res)))