def f(n):
    if n == 1 or n == 0:
        return 1
    return f(n-1)*n

n = int(input())
print(f(n))