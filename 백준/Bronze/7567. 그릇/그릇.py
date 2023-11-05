ans = 0
prev = ""
for char in input():
    if char == prev:
        ans += 5
    else:
        ans += 10
        prev = char
print(ans)