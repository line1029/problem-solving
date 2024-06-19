class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums) - 1
        for k in range(j, -1, -1):
            if nums[k] != val:
                break
        else:
            return 0
        j = k
        while i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                while i < j and nums[j] == val:
                    j -= 1
                if i == j:
                    return i + 1
            i += 1
        return i + 1