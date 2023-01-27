from sys import stdin
n = int(stdin.readline())
seq = list(map(int, stdin.readlines()))
k = len(seq)
stack = []
idx = 0
cur = 1
ans = []
while idx < k:
    while cur <= seq[idx]:
        stack.append(cur)
        ans.append("+")
        cur += 1
    while stack and stack[-1] == seq[idx]:
        stack.pop()
        ans.append("-")
        idx += 1
    if idx < k and seq[idx] < cur:
        print("NO")
        break
else:
    print("\n".join(ans))