from sys import stdin, stdout
from collections import Counter

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
cnts = Counter(arr)
ans = [-1] * n
st = []
for idx, num in enumerate(arr):
    while st and cnts[arr[st[-1]]] < cnts[num]:
        ans[st.pop()] = num
    st.append(idx)
stdout.write(" ".join(map(str, ans)))
