from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
wtod = dict()
dtow = dict()
for i in range(1, n+1):
    name = stdin.readline().strip()
    wtod[name] = str(i)
    dtow[str(i)] = name
for _ in range(m):
    query = stdin.readline().strip()
    if query.isdigit():
        stdout.write(f"{dtow[query]}\n")
    else:
        stdout.write(f"{wtod[query]}\n")