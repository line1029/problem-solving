class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_dict = dict()
        nums_set = set()
        for idx, num in enumerate(nums):
            nums_dict[-num] = idx
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in nums_dict and nums_dict[nums[i] + nums[j]] > j:
                    nums_set.add((nums[i], nums[j], nums[nums_dict[nums[i] + nums[j]]]))
        return [list(i) for i in nums_set]