from sys import stdin

n = int(stdin.readline())
print("\n".join(f"{i*'*':>{n}}" for i in range(1, n + 1)))
