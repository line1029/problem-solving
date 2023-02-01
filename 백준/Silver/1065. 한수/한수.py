s = [True] * 99 + [False] * 901
for i in range(111, 1000):
    if i // 100 + i % 10 == (i // 10 % 10) * 2:
        s[i - 1] = True
print(sum(s[:int(input())]))