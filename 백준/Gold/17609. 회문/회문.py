from sys import stdin
stdin.readline()
for s in stdin.read().splitlines():
    if s == s[::-1]:
        print(0)
        continue
    n = len(s)
    i, j = 0, n - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    if s[i + 1:j + 1] == s[j:i:-1] or s[i:j] == s[j - 1:i - 1:-1] or s[i:j] == s[j - 1::-1]:
        print(1)
    else:
        print(2)