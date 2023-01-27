n = int(input())
ans = 0
while n:
    n //= 5
    ans += n
print(ans)