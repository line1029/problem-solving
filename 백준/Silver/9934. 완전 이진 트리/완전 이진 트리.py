from sys import stdin, stdout
def main():
    k = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    ans = []
    for i in range(k):
        ans.append(" ".join(map(str, arr[(1 << i) - 1::1 << (i + 1)])))
    stdout.write("\n".join(reversed(ans)))
main()