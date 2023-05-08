n, k = map(int, input().split())
binary = f"{n:b}"
ones = binary.count("1")
ans = 0
while ones > k:
    idx = binary[::-1].index("1")
    n += 1 << idx
    ans += 1 << idx
    binary = f"{n:b}"
    ones = binary.count("1")
print(ans)