n = int(input())
s = input()
r = 31
q = 1
M = 1234567891
ans = 0
for char in s:
    num = ord(char) - 96
    ans += num * q
    ans %= M
    q *= r
    q %= M
print(ans)