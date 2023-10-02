from sys import stdin
arr = list(map(lambda x: sorted(map(int, x.split())), stdin.read().splitlines()))
arr.pop()
for i, (a, b, c) in enumerate(arr):
    if a + b <= c:
        arr[i] = "Invalid"
    elif a == b == c:
        arr[i] = "Equilateral"
    elif a == b or b == c:
        arr[i] = "Isosceles"
    else:
        arr[i] = "Scalene"
print("\n".join(arr))