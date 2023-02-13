from sys import stdin
n, m = map(int, stdin.readline().split())
s = stdin.readline().strip()[::-1]
vowel = {"A", "E", "I", "O", "U"}
for i in range(n):
    if s[i] not in vowel:
        first = i
        break
else:
    print("NO")
    exit()
if first > n - 3:
    print("NO")
    exit()
for i in range(first + 1, n):
    if s[i] == "A":
        second = i
        break
else:
    print("NO")
    exit()
if second > n - 2:
    print("NO")
    exit()
for i in range(second + 1, n):
    if s[i] == "A":
        third = i
        break
else:
    print("NO")
    exit()
left = n - third - 1
if left < m - 3:
    print("NO")
    exit()
ans = s[first] + "AA" + s[third + 1: third + m - 2]
print("YES")
print(ans[::-1])