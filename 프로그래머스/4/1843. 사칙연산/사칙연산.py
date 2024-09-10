from functools import lru_cache
import operator

def solution(arr):
    oper_map = {
        "+": operator.add,
        "-": operator.sub
    }
    arr = list(map(lambda x: oper_map[x] if x in oper_map else int(x), arr))
    
    @lru_cache(maxsize=None)
    def dp(start, end, is_max=True):
        if start == end:
            return arr[start]
        if not is_max:
            stack = []
            cur = arr[start]
            for i in range(start, end, 2):
                if arr[i + 1] is operator.add:
                    cur += arr[i + 2]
                else:
                    stack.append(cur)
                    cur = arr[i + 2]
            stack.append(cur)
            return 2 * stack[0] - sum(stack)
        ans = - 101000
        for mid in range(start, end, 2):
            ans = max(
                ans,
                arr[mid + 1](dp(start, mid), dp(mid + 2, end)),
                arr[mid + 1](dp(start, mid), dp(mid + 2, end, False))
            )
                
        return ans
    return dp(0, len(arr) - 1)
            