from sys import stdin, stdout

res = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    applies = [0] * n
    for __ in range(n):
        i, j = map(int, stdin.readline().split())
        applies[i - 1] = j
    cur = applies[0]
    ans = 1
    for j in applies:
        if j < cur:
            ans += 1
            cur = j
        if cur == 1:
            break
    res.append(ans)
stdout.write("\n".join(map(str, res)))
