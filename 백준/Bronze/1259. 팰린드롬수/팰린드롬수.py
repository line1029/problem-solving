from sys import stdin, stdout
nums = list(map(lambda x: x.strip(), stdin.readlines()))
idx = 0
n = len(nums)
while idx < n - 1:
    if nums[idx] == nums[idx][::-1]:
        stdout.write("yes\n")
    else:
        stdout.write("no\n")
    idx += 1