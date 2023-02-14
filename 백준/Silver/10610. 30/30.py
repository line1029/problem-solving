from sys import stdin
n = sorted(stdin.readline().rstrip(), reverse=True)
if sum(map(int, n))%3 == 0 and n[-1] == "0":
    print("".join(n))
else:
    print(-1)