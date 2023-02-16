n, k = map(int, input().split())
people = list(range(1, n + 1))
ans = []
idx = 0
while people:
    idx = (idx + k - 1) % len(people)
    ans.append(people.pop(idx))
print("<" + ", ".join(map(str, ans)) + ">")