from sys import stdin
from itertools import islice
from math import floor
n = int(stdin.readline())
def round(num):
    return floor(num + 0.5)
if not n:
    print(0)
    exit()
outlier = round(n*0.15)
scores = sorted(map(int, stdin.read().splitlines()))
print(round(sum(islice(scores, outlier, n - outlier)) / (n - 2*outlier)))