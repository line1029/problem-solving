s = input()
ans = 1
prev = None
for char in s:
    if prev != char:
        if char == "c":
            cnt = 26
        else:
            cnt = 10
    else:
        if char == "c":
            cnt = 25
        else:
            cnt = 9
    ans *= cnt
    prev = char
print(ans)