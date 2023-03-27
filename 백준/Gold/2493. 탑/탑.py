from sys import stdin, stdout
input = stdin.readline
n = int(input())
towers = map(int, reversed(input().split()))
stack = []
ans = [0]*n
for idx, height in enumerate(towers):
    if stack and stack[-1][1] < height:
        while stack and stack[-1][1] < height:
            ans[stack[-1][0]] = n - idx
            stack.pop()
    stack.append((n - idx - 1, height))
stdout.write(" ".join(map(str, ans)))