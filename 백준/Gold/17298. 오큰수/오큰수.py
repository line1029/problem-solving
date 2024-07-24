from sys import stdin, stdout
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
ans = [-1] * n
st = []
for idx, num in enumerate(arr):
    while st and arr[st[-1]] < num:
        i = st.pop()
        ans[i] = num
    st.append(idx)
stdout.write(" ".join(map(str, ans)))