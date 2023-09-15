from sys import stdin
def main():
    n, m, k = map(int, stdin.readline().split())
    if n&1:
        n -= 1
        k -= 1
    if n > 2*m:
        k -= n - 2*m
        n = 2*m
    else:
        k -= m - n//2
        m = n//2
    if k <= 0:
        print(m)
    else:
        print(m - (k + 2)//3)
main()