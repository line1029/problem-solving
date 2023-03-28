s = input()
l, r = [], [s[0]]
n = len(s)
for i in range(1, n):
    if s[i] > r[-1]:
        l.append(s[i])
    else:
        r.append(s[i])
print("".join(r[::-1] + l))