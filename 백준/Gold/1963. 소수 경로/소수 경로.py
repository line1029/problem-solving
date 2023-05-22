from sys import stdin
from collections import deque
sieve = [False, True] * 5000
sieve[1] = False
sieve[2] = True
for i in range(2, 100):
    if sieve[i]:
        sieve[i*i::i] = len(sieve[i*i::i]) * [False]
primes = set(i for i in range(1000, 10000) if sieve[i])

grid = dict()
for prime in primes:
    grid[prime] = []
    for digit_num in range(4):
        base = prime - (prime // 10**digit_num % 10) * 10**digit_num
        for digit in range(10):
            candidate = base + digit * 10**digit_num
            if candidate != prime and candidate in primes:
                grid[prime].append(candidate)

def bfs(start, end):
    if start == end:
        return 0
    queue = deque([start])
    visited = {start}
    depth = 0
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            for nex in grid[cur]:
                if nex == end:
                    return depth + 1
                if nex not in visited:
                    visited.add(nex)
                    queue.append(nex)
        depth += 1
            

for _ in range(int(stdin.readline())):
    step = bfs(*map(int, stdin.readline().split()))
    if step is not None:
        print(step)
    else:
        print("Impossible")