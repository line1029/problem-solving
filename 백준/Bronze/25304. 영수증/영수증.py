import sys
total = int(sys.stdin.readline())
n = int(sys.stdin.readline())
cal = 0
for i in range(n):
    price, num = map(int, sys.stdin.readline().split())
    cal += price*num
if total == cal:
    print("Yes")
else:
    print("No")