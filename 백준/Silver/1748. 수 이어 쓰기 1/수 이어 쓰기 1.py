n = input()
k = len(n)
if k == 1:
    print(n)
    exit()
ans = (k - 1)*10**(k-1) - 1 - 10*(10**(k-2)-1)//9 + (int(n) - 10**(k-1) + 1)*k
print(ans)