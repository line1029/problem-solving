h, m = map(int, input().split())
if m >= 45:
    print(h, m - 45)
else:
    print((h - 1) % 24, (m - 45) % 60)