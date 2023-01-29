from sys import stdin
n = int(stdin.readline())
people = list(map(int, stdin.readline().split()))
people.sort()
ans = 0
for idx, num in enumerate(people):
    ans += (n-idx)*num
print(ans)