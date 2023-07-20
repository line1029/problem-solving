from sys import stdin
def f(x1, y1, x2, y2, z1, w1, z2, w2):
    if x2 < z1 or z2 < x1 or y2 < w1 or w2 < y1:
        return "d"
    if (x1 == z2 or x2 == z1) and (y1 == w2 or y2 == w1):
        return "c"
    if (x1 == z2 or x2 == z1):
        if y2 > w1 and w2 > y1:
            return "b"
    if (y1 == w2 or y2 == w1):
        if x2 > z1 and z2 > x1:
            return "b"
    return "a"
def main():
    ans = []
    for i in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        ans.append(f(*i))
    print("\n".join(ans))
main()