from sys import stdin, stdout
linear_sieve = [0]*5000001
primes = []
for i in range(2, 5000001):
    if not linear_sieve[i]:
        primes.append(i)
        linear_sieve[i] = i
    for j in primes:
        if j * i > 5000000:
            break
        linear_sieve[j * i] = j
        if i % j == 0:
            break
n = int(stdin.readline())
ans = []
for num in map(int, stdin.readline().split()):
    tmp = []
    while num != 1:
        tmp.append(linear_sieve[num])
        num //= linear_sieve[num]
    ans.append(" ".join(map(str, tmp)))
stdout.write("\n".join(ans))