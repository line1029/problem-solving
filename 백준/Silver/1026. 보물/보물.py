m = int(input())
a, b = sorted(map(int, input().split())), sorted(map(int, input().split()), reverse=True)
print(sum(i * j for i, j in zip(a, b)))