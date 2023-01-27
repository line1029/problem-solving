nums = list(map(lambda x: sum(map(int, x.split("+"))),input().split("-")))
print(nums[0]*2 - sum(nums))