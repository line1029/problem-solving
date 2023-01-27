n = int(input())
m = int(input())
min_val = abs(n - 100)
if m == 0:
    min_val = min(min_val, len(str(n)))
else:
    from itertools import product
    cannot = set(input().split())
    can = set(map(str, range(10))).difference(cannot)
    for num in product(can, repeat=len(str(n))):
        num1 = int("".join(num))
        min_val = min(min_val, abs(n-num1) + len(num))
        if len(num) >= 2:
            num2 = int("".join(num[:-1]))
            min_val = min(min_val, abs(n-num2) + len(num) - 1)
        if "1" in can:
            num3 = int("1"+"".join(num))
            min_val = min(min_val, abs(n-num3) + len(num) + 1)
print(min_val)