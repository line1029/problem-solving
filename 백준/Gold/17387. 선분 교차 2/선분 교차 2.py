from sys import stdin
def ccw(a, b, c):
    return (b[0] - a[0])*(c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0])

def main():
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    x3, y3, x4, y4 = map(int, stdin.readline().split())
    a, b = (x1, y1), (x2, y2)
    c, d = (x3, y3), (x4, y4) 
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    l1, l2 = ccw(a, b, c)*ccw(a, b, d), ccw(c, d, a)*ccw(c, d, b)
    if not l1 and not l2:
        if a <= d and b >= c:
            print(1)
        else:
            print(0)
    elif l1 <= 0 and l2 <= 0:
        print(1)
    else:
        print(0)

main()