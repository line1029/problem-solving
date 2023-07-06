from sys import stdin, stdout
from math import comb
def main():
    stdin.readline()
    ans = []
    for n, m in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        ans.append(comb(m, n))
    stdout.write("\n".join(map(str, ans)))

main()