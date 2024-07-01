class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not n:
            return
        if not m:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        for i in range(m + n - 1, n - 1, -1):
            nums1[i] = nums1[i - n]
        j = k = 0
        while i < m + n and j < n:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        while j < n:
            nums1[k] = nums2[j]
            j += 1
            k += 1

        