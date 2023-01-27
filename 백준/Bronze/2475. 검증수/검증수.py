from sys import stdin
print(sum(map(lambda x: int(x)**2, stdin.readline().split()))%10)
