from sys import setrecursionlimit
def solution(k, num, links):
    setrecursionlimit(100000)
    parents = [-1]*len(num)
    for idx, (i, j) in enumerate(links):
        if i != -1:
            parents[i] = idx
        if j != -1:
            parents[j] = idx
    root = parents.index(-1)
    
    def dfs(root, limit):
        left_sum = right_sum = left_split = right_split = 0
        if links[root][0] != -1:
            left_sum, left_split = dfs(links[root][0], limit)
        if links[root][1] != -1:
            right_sum, right_split = dfs(links[root][1], limit)
        if num[root] + left_sum + right_sum <= limit:
            return num[root] + left_sum + right_sum, left_split + right_split
        elif num[root] + left_sum > limit and num[root] + right_sum > limit:
            return num[root], left_split + right_split + 2
        else:
            return num[root] + min(left_sum, right_sum), left_split + right_split + 1

    hi = sum(num)
    lo = max(max(num), hi//k)
    while lo < hi:
        mid = (lo + hi) >> 1
        _, num_split = dfs(root, mid)
        if num_split < k:
            hi = mid
        else:
            lo = mid + 1
    return lo