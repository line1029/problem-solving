from sys import stdin
for s in stdin.read().splitlines():
    if s == "END": break
    print(s[::-1])