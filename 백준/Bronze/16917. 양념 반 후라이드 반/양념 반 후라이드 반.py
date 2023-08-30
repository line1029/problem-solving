from sys import stdin
def main():
    a, b, c, x, y = map(int, stdin.readline().split())
    ans = 0
    if (c << 1) < a + b:
        z = min(x, y)
        ans += 2*z*c
        x -= z
        y -= z
    ans += min(a*x + b*y, 2*c*(x + y))
    print(ans)
main()