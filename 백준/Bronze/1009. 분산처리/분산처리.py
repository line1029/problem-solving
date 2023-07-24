from sys import stdin
def main():
    t = int(stdin.readline())
    ans = [0]*t
    for i in range(t):
        ans[i] = pow(*map(int, stdin.readline().split()), 10)
        if not ans[i]:
            ans[i] = 10
    print("\n".join(map(str, ans)))
main()