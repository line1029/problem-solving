from sys import stdin, stdout
n, _ = map(int, stdin.readline().split())
names = stdin.read().rstrip().split("\n")
sn, sm = set(names[:n]), set(names[n:])
ans = sorted(list(sn.intersection(sm)))
print(len(ans))
stdout.write("\n".join(ans))