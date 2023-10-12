n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())
ans = n
for i in arr:
    if i > b:
        ans += (i - b) // c + (((i - b) % c) != 0)
print(ans)
