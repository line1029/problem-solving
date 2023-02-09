from collections import Counter
from itertools import islice
from sys import stdin
n, k = map(int, stdin.readline().split())
students = list(map(len, stdin.read().splitlines()))
good_friends = Counter(islice(students, k + 1))
ans = 0
for i in range(n - k - 1):
    good_friends[students[i]] -= 1
    ans += good_friends[students[i]]
    good_friends[students[i + k + 1]] += 1
for i in range(n - k - 1, n - 1):
    good_friends[students[i]] -= 1
    ans += good_friends[students[i]]
print(ans)