from sys import stdin
def main():
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    z1, w1, z2, w2 = map(int, stdin.readline().split())
    if y2 < w1 or w2 < y1 or x2 < z1 or z2 < x1:
        return "NULL"
    if (x2 == z1 or x1 == z2) and (y2 == w1 or y1 == w2):
        return "POINT"
    if (x2 == z1 or x1 == z2):
        if y2 > w1 and w2 > y1:
            return "LINE"
    if (y2 == w1 or y1 == w2):
        if x2 > z1 and z2 > x1:
            return "LINE"
    return "FACE"
print(main())