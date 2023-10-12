p = int(input())
for _ in range(p):
    t, m = map(int, input().split())
    a = b = 1
    for i in range(1, m*m):
        a, b = b, (a + b)%m
        if a == b == 1:
            print(t, i)
            break
