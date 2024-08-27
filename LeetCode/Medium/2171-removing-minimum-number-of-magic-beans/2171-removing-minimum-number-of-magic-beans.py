class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        p_sum = list(itertools.accumulate(beans, initial=0))
        return min(p_sum[idx] - p_sum[idx + 1] + p_sum[-1] - b * (n - idx - 1) for idx, b in enumerate(beans))