from sys import stdin, stdout
def main():
    n, q = map(int, stdin.readline().split())
    ans = []
    inv = 0
    for a, l, r in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        if a == 1 or ((r - l + 1) >> 1) & 1:
            inv = 0 if inv else 1
        ans.append(inv)
    stdout.write("\n".join(map(str, ans)))
main()