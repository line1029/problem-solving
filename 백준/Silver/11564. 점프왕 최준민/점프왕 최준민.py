k, a, b = map(int, input().split())
ak = a//k + (a%k != 0)
bk = b//k
print(bk - ak + 1)