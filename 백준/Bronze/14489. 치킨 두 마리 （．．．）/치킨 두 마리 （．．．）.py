a = sum(map(int, input().split()))
b = int(input())
if a >= 2*b:
    a -= 2*b
print(a)