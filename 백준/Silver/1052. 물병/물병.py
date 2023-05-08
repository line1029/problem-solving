n, k = map(int, input().split())
binary = f"{n:b}"
ones = binary.count("1")
m = n
while ones > k:
    n += 1
    binary = f"{n:b}"
    ones = binary.count("1")
print(n - m)