from sys import stdin
k, n = map(int, stdin.readline().split())
lan = list(map(int, stdin.readlines()))
def net_lans(num, lan):
    return sum(i//num for i in lan)
lo, hi = 1, max(lan)
while lo <= hi:
    mi = (lo + hi)//2
    if net_lans(mi, lan) < n:
        hi = mi - 1
    else:
        lo = mi + 1
print(hi)