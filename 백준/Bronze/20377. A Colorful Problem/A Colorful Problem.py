from sys import stdin
def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2
def main():
    targets = [list(map(int, stdin.readline().split())) for _ in range(16)]
    colors = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    cmaps = []
    for c in colors:
        idx = 0
        d = dist(c, targets[0])
        for i, t in enumerate(targets):
            nd = dist(c, t)
            if nd < d:
                d = nd
                idx = i
        cmaps.append(targets[idx])
    print("\n".join(f"{c[0]:>3} {c[1]:>3} {c[2]:>3} maps to {m[0]:>3} {m[1]:>3} {m[2]:>3}" for c, m in zip(colors, cmaps)))
main()