from sys import stdin
def main():
    n = int(stdin.readline())
    ans = ["no"]*n
    for i in range(n):
        a, b, c = sorted(map(int, stdin.readline().split()))
        if a*a + b*b - c*c == 0:
            ans[i] = "yes"
    print("\n\n".join(f"Scenario #{i}:\n{x}" for i, x in enumerate(ans, 1)))
main()
