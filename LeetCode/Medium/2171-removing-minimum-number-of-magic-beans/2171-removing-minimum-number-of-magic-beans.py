class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        p_sum = [0] * (n + 1)
        for idx, b in enumerate(beans, 1):
            p_sum[idx] += p_sum[idx - 1] + b
        ans = p_sum[-1]
        for idx, b in enumerate(beans):
            num = p_sum[idx] - p_sum[idx + 1] + p_sum[-1] - b * (n - idx - 1)
            ans = min(ans, num)
        return ans