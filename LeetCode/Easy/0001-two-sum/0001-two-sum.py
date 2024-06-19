class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxs = {}
        for idx, num in enumerate(nums):
            if target - num in idxs:
                return [idx, idxs[target - num]]
            idxs[num] = idx