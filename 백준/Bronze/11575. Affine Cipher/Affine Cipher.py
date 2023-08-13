from sys import stdin
def main():
    t = int(stdin.readline())
    ans = [""]*t
    for i in range(t):
        a, b = (map(int, stdin.readline().split()))
        ans[i] = "".join(map(lambda x: chr((a*(ord(x) - 65) + b)%26 + 65), stdin.readline().strip()))
    print("\n".join(ans))

main()
