n = int(input())
# 3x + 5y = n
# x, y = [-3n + k//3, 2n - k//5],  15|k
x = -3*n
y = 2*n
k = (3*n//5 + (3*n%5 != 0))*15
if y - k//5 < 0:
    print(-1)
else:
    print(k//3 - k//5 - n)