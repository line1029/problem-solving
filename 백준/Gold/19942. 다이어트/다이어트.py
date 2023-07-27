from sys import stdin
from itertools import combinations
def main():
    n = int(stdin.readline())
    mp, mf, ms, mv = map(int, stdin.readline().split())
    ans = 10000
    idxs = []
    ingredients = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    for i in range(n):
        ingredients[i].insert(0, i + 1)
    for i in range(1, n + 1):
        for pats in combinations(ingredients, i):
            p = f = s = v = c = 0
            for _, p_, f_, s_, v_, c_ in pats:
                p += p_
                f += f_
                s += s_
                v += v_
                c += c_
                if ans < c:
                    break
            else:
                if p >= mp and f >= mf and s >= ms and v >= mv:
                    if ans > c:
                        ans = c
                        idxs = [i[0] for i in pats]
                    elif idxs > [i[0] for i in pats]:
                        idxs = [i[0] for i in pats]
    if ans != 10000:
        print(ans)
        print(*idxs)
    else:
        print(-1)
main()