from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().rstrip()
l, r = 0, 0
cnt = 0
while r < m and s[r] != "I":
    r += 1
l = r
while r < m:
    if r < m - 1 and ((s[r] == "I" and s[r+1]=="O") or (s[r] == "O" and s[r+1]=="I")):
        r += 1
    else:
        if r == m-1:
            break
        while s[r] != "I" or (r < m-1 and s[r] == "I" and s[r+1]!="O"):
            r += 1
        l = r
    if r - l == 2*n:
        cnt += 1
        l += 2
print(cnt)