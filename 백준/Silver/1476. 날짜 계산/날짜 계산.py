from sys import stdin
e, s, m = map(int, stdin.readline().split())
# Since 15, 28, 19 are coprime, we can use Chinese Remainder Theorem
# mod = 15*28*19 = 7980
mod = 7980
# n1 = 28*19 = 532
n1 = 532
# n2 = 15*19 = 285
n2 = 285
# n3 = 15*28 = 420
n3 = 420
# n1*s1 == 532*s1 == 7*s1 == 1 (mod 15)
s1 = 13
# n2*s2 == 285*s2 == 5*s2 == 1 (mod 28)
s2 = 17
# n3*s3 == 420*s3 == 2*s3 == 1 (mod 19)
s3 = 10
ans = (e*n1*s1 + s*n2*s2 + m*n3*s3)%mod
if not ans:
    ans = mod
print(ans)
