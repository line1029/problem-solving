n, r, c = map(int, input().split())
r2 = bin(r)[:1:-1]
c2 = bin(c)[:1:-1]
r2 += "0"*(n-len(r2))
c2 += "0"*(n-len(c2))
coo = 0
for idx in range(n):
    coo += (2*int(r2[idx])+int(c2[idx]))*4**idx
print(coo)