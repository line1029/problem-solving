from sys import stdin
from math import sqrt, pi
circles = stdin.read().splitlines()
for c in circles:
    x1, y1, x2, y2, x3, y3 = map(float, c.split())
    a = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2))
    b = sqrt(pow(x1-x3, 2) + pow(y1-y3, 2))
    c = sqrt(pow(x3-x2, 2) + pow(y3-y2, 2))
    s = (a+b+c)/2
    r = 2*pi*a*b*c/(4*sqrt(s*(s-a)*(s-b)*(s-c)))
    print(round(r, 2))