data1 = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="}
data2 = {"c", "d", "l", "n", "s", "z"}

s = input()
n = len(s)
idx = 0
ans = 0
while idx < n:
    if s[idx] in data2:
        if s[idx:idx + 2] in data1:
            idx += 2
        elif s[idx:idx + 3] in data1:
            idx += 3
        else:
            idx += 1
    else:
        idx += 1
    ans += 1
print(ans)
