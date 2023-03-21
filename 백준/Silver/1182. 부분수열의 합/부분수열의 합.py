from sys import stdin
input = stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = [0]
def backtracking(cur_idx, cur_sum):
    if cur_idx == n:
        return
    
    cur_sum += arr[cur_idx]

    if cur_sum == s:
        ans[0] += 1
    backtracking(cur_idx + 1, cur_sum - arr[cur_idx])
    backtracking(cur_idx + 1, cur_sum)


backtracking(0, 0)
print(ans[0])