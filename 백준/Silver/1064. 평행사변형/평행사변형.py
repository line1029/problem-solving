x1, y1, x2, y2, x3, y3 = map(int, input().split())
from math import gcd
g1, g2 = gcd(x1-x2, y1-y2), gcd(x1-x3, y1-y3)
if ((x1-x2)//g1 == (x1-x3)//g2 and (y1-y2)//g1 == (y1-y3)//g2) or \
    ((x1-x2)//g1 == -(x1-x3)//g2 and -(y1-y2)//g1 == (y1-y3)//g2):
    print(-1.)
    exit()
def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**.5
triangle_edge = [distance(x1, y1, x2, y2), distance(x1, y1, x3, y3), distance(x3, y3, x2, y2)]
triangle_edge.sort()
print((triangle_edge[2] - triangle_edge[0])*2)
