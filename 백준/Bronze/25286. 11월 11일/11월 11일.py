a = [0, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [0, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
for _ in range(int(input())):
    y, m = map(int, input().split())
    mm = a[m]
    dd = b[m]
    if m == 1:
        y -= 1
    if m == 3 and not y%4 and y != 2100:
        dd += 1
    print(y, mm, dd)