from sys import stdin, stdout
n = int(stdin.readline())
arr = [[i, 1] for i in list(range(n))]
for i in range(n):
    arr[i].extend(map(int, stdin.readline().split()))
arr.sort(key=lambda x: (x[2], x[3]))
for i in range(n):
    for j in range(i+1, n):
        if arr[i][2] < arr[j][2] and arr[i][3] < arr[j][3]:
            arr[i][1] += 1
ans = [""]*n
for info in arr:
    ans[info[0]] = str(info[1])
    
print(" ".join(ans))