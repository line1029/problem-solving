from sys import stdin
def main():
    a, b, c = map(int, stdin.readline().split())
    if a == b:
        return 0
    ans = min(a + b + c, a*b*c)
    d = a + b
    ans = min(ans, d * c)
    if d - c >= 0:
        ans = min(ans, d - c)
    if not d % c:
        ans = min(ans, d//c)
    d = a - b
    if d > 0:
        ans = min(ans, d * c, d + c)
        if d - c >= 0:
            ans = min(ans, d - c)
        if not d % c:
            ans = min(ans, d//c)
    else:
        if d + c >= 0:
            ans = min(ans, d + c)
    d = a * b
    ans = min(ans, d * c, d + c)
    if d - c >= 0:
        ans = min(ans, d - c)
    if not d % c:
        ans = min(ans, d//c)
    if not a % b:
        d = a // b
        ans = min(ans, d * c, d + c)
        if d - c >= 0:
            ans = min(ans, d - c)
        if not d % c:
            ans = min(ans, d//c)
    return ans
print(main())