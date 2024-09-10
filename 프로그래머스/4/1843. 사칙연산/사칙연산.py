import operator

def solution(arr):
    operation_map = [
        "+",
        "-"
    ]
    # arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
    arr = list(map(lambda x: int(x) if x not in operation_map else x, arr))
    # arr = [5, "-", 3, "+", 1, "+", 2, "-", 4]
    n = len(arr)
    INF = 1_000_000
    dp_max = [[-INF] * n for _ in range(n)]
    dp_min = [[INF] * n for _ in range(n)]
    for i in range(0, n + 1, 2):
        dp_max[i][i] = arr[i]
        dp_min[i][i] = arr[i]
    
    def dp(start, end, is_max=True):
        if is_max:
            if dp_max[start][end] != -INF:
                return dp_max[start][end]
            ans = -INF
            for mid in range(start, end, 2):
                if arr[mid + 1] == "+":
                    ans = max(ans, (dp(start, mid) + dp(mid + 2, end)))
                else:
                    ans = max(ans, (dp(start, mid) - dp(mid + 2, end, False)))
            dp_max[start][end] = ans
            return ans
        else:
            if dp_min[start][end] != INF:
                return dp_min[start][end]
            stack = []
            cur = arr[start]
            for idx in range(start, end, 2):
                if arr[idx + 1] == "+":
                    cur += arr[idx + 2]
                else:
                    stack.append(cur)
                    cur = arr[idx + 2]
            stack.append(cur)
            ans = 2 * stack[0] - sum(stack)
            dp_min[start][end] = ans
            return ans
            
    return dp(0, n - 1)
    