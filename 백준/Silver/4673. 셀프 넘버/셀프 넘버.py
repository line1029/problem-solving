arr = [True] * 10000
idx = 0
while idx < 10000:
    if arr[idx]:
        n = idx + 1
        while n < 10000:
            n = n + n//10000 + n//1000%10 + n//100%10 + n//10%10 + n%10
            if n < 10001:
                arr[n - 1] = False
    idx += 1
for i, p in enumerate(arr):
    if p:
        print(i + 1)
        

                