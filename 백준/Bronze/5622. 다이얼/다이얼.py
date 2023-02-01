data = {}
for i in range(65, 91):
    if i < 83:
        data[chr(i)] = (i - 65) // 3 + 2
    elif i == 83:
        data["S"] = 7
    elif 83 < i < 87:
        data[chr(i)] = 8
    else:
        data[chr(i)] = 9

ans = 0
for s in input():
    ans += data[s] + 1
print(ans)
