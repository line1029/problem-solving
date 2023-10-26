s, t = input(), input()
i, j = 0, len(t) - 1
rev = False
for _ in range(len(t) - len(s)):
    if rev:
        if t[i] == "B":
            rev = not rev
        i += 1
    else:
        if t[j] == "B":
            rev = not rev
        j -= 1
print(int(s == (t[j:i - 1:-1] if rev and i else t[j::-1] if rev else t[i:j + 1])))