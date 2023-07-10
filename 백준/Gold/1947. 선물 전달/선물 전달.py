n = int(input())
MOD = 1_000_000_000
if n <= 2:
    print(n - 1)
    exit()
a, b = 0, 1
for i in range(3, n + 1):
    c = (i - 1)*(a + b)
    a = b
    b = c%MOD
print(b)