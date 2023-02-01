n = int(input())
num = 0
while num < n:
    if num + sum(list(map(int, str(num)))) == n:
        print(num)
        break
    num += 1
if num == n:
    print(0)