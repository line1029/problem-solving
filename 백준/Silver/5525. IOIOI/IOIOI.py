from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
ioi = stdin.readline().rstrip().replace("II", "IOOI").split("OO")
leng = 2*n + 1
cnt = 0
for s in ioi:
    k = len(s)
    if not k:
        continue
    k -= (s[0] == "O") + (s[-1] == "O")
    if k - leng < 0:
        continue
    cnt += (k - leng)//2 + 1
print(cnt)