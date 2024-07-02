class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        zero_twice = 0
        for i in nums:
            if i:
                p *= i
            else:
                zero_twice += 1
                if zero_twice == 2:
                    return [0] * len(nums)
        if zero_twice:
            return [(0 if i else p) for i in nums]
        return [p//i for i in nums]