class Solution:
    def hIndex(self, citations: List[int]) -> int:
        lo, hi = 0, len(citations)
        n = hi
        while lo < hi:
            mid = (lo + hi) >> 1
            if n - mid <= citations[mid]:
                hi = mid
            else:
                lo = mid + 1
        return n - lo