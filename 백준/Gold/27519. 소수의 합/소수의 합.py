from sys import stdin, stdout
M = 1_000_000_007
t = int(stdin.readline())
nums = list(map(int, stdin.read().splitlines()))
n = max(nums)
sieve = [False, True] * (n // 2 + 1)
sieve[1] = False
if n >= 2:
    sieve[2] = True
for i in range(3, int(n**.5) + 1, 2):
    if sieve[i]:
        sieve[i*i::i*2] = [False] * len(sieve[i*i::i*2])
primes = [i for i, b in enumerate(sieve) if b]
dp = [0] * (n + 1)
dp[0] = 1
for prime in primes:
    for k in range(prime, n + 1):
        dp[k] += dp[k - prime]
        dp[k] %= M
stdout.write("\n".join(map(lambda x: str(dp[x]), nums)))
