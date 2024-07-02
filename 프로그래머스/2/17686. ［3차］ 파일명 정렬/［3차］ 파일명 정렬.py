import re
def ordering(s):
    n = re.search(r"\d+", s)
    head = s[:n.start()].lower()
    nums = int(n.group())
    return head, nums
def solution(files):
    files.sort(key=ordering)
    return files