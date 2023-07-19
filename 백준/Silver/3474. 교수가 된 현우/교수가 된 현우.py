from sys import stdin

def main():
    t = int(stdin.readline())
    ans = [0]*t
    for idx, num in enumerate(map(int, stdin.read().splitlines())):
        while num:
            ans[idx] += num//5
            num //= 5
    print("\n".join(map(str, ans)))
main()