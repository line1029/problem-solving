from sys import stdin, stdout
n = int(stdin.readline())
candidates = set(map(int, stdin.readline().split()))
m = int(stdin.readline())
ans = ("1" if i in candidates else "0" for i in map(int, stdin.readline().split()))
stdout.write("\n".join(ans))