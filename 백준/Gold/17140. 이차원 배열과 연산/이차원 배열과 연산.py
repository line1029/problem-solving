from sys import stdin
r, c, K = map(int, stdin.readline().split())
r -= 1
c -= 1
a = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
for time in range(101):
    if r < len(a) and c < len(a[0]) and a[r][c] == K:
        print(time)
        exit()
    # R operation
    if len(a) >= len(a[0]):
        tmp_a = [[] for _ in range(len(a))]
        for i in range(len(a)):
            d = dict()
            for j in range(len(a[0])):
                if a[i][j] not in d:
                    d[a[i][j]] = 1
                else:
                    d[a[i][j]] += 1
            for k, v in sorted(d.items(), key=lambda x:(x[1], x[0])):
                if not k: continue
                tmp_a[i].append(k)
                tmp_a[i].append(v)
        l = max(len(tmp_a[i]) for i in range(len(a)))
        for i in range(len(a)):
            if len(tmp_a[i]) < l:
                tmp_a[i] += [0]*(l - len(tmp_a[i]))
        a = tmp_a
    # C operation
    else:
        tmp_a = [[] for _ in range(len(a[0]))]
        for i in range(len(a[0])):
            d = dict()
            for j in range(len(a)):
                if a[j][i] not in d:
                    d[a[j][i]] = 1
                else:
                    d[a[j][i]] += 1
            for k, v in sorted(d.items(), key=lambda x:(x[1], x[0])):
                if not k: continue
                tmp_a[i].append(k)
                tmp_a[i].append(v)
        l = max(len(tmp_a[i]) for i in range(len(tmp_a)))
        for i in range(len(tmp_a)):
            if len(tmp_a[i]) < l:
                tmp_a[i] += [0]*(l - len(tmp_a[i]))
        a = [[tmp_a[i][j] for i in range(len(tmp_a))] for j in range(len(tmp_a[0]))]
print(-1)