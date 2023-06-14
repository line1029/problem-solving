from sys import stdin, stdout
stack = []
n = int(stdin.readline())
towers = list(map(int, stdin.readline().split()))
view = [0] * n
view_reverse = [0] * n
closest = [0] * n
dist = [100001] * n
for i, x in enumerate(towers):
    while stack and stack[-1][0] <= x:
        stack.pop()
    if stack:
        j = stack[-1][1]
        view[i] = view[j] + 1
        if dist[i] > i - j:
            dist[i] = i - j
            closest[i] = j + 1
    stack.append((x, i))
stack.clear()
for i in range(n - 1, -1, -1):
    x = towers[i]
    while stack and stack[-1][0] <= x:
        stack.pop()
    if stack:
        j = stack[-1][1]
        view_reverse[i] = view_reverse[j] + 1
        if dist[i] > j - i:
            dist[i] = j - i
            closest[i] = j + 1
    stack.append((x, i))
ans = [f"{view[i] + view_reverse[i]} {closest[i]}" if view[i] + view_reverse[i] else "0" for i in range(n)]

stdout.write("\n".join(ans))