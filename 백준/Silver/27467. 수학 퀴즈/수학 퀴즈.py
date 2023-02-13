from sys import stdin
n = int(stdin.readline())
def get_coefficient(a):
    a = int(a)
    if a%3 == 0:
        return 0, 1
    elif a%3 == 1:
        return 1, 0
    else:
        return -1, -1
arr = map(get_coefficient, stdin.readline().split())
ans = [0, 0]
for c1, c2 in arr:
    ans[0] += c1
    ans[1] += c2
print(" ".join(map(str, ans)))