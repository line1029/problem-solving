from sys import stdin
arr = list(map(int, stdin.readline().split()))
ans = [1, 2, 3, 4, 5, 6, 7, 8]
if arr == ans:
    print("ascending")
elif arr == ans[::-1]:
    print("descending")
else:
    print("mixed")