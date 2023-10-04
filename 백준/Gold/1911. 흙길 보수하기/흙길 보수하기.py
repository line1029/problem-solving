from sys import stdin
n, l = map(int, stdin.readline().split())
pool = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
cur = pool[0][0] + l
ans = 1
for start, end in pool:
    if end <= cur: continue
    if start < cur: start = cur
    need = (end - start)//l + ((end - start)%l != 0)
    ans += need
    cur = start + need*l
print(ans)
