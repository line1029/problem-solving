from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
psum_left = [0]
psum_right = [0]
for i in range(n):
    psum_left.append(psum_left[-1] + arr[i])
    psum_right.append(psum_right[-1] + arr[-i - 1])
ans = psum_left[-2] - psum_left[1] + max(arr[1:-1])
for i in range(2, n):
    ans = max(
        ans,
        2*psum_left[-1] - psum_left[1] - psum_left[i] - arr[i - 1],
        2*psum_right[-1] - psum_right[1] - psum_right[i] - arr[-i]    
    )
print(ans)