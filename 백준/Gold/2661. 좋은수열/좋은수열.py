n = int(input())
arr = [1, 2, 1, 3, 1, 2]
s = [1, 2, 3]
def dfs(depth):
    if depth == n:
        print("".join(map(str, arr)))
        exit()
    for i in s:
        arr.append(i)
        for length in range(1, (depth + 1)//2 + 1):
            if arr[depth + 1 - 2*length:depth + 1 - length] == arr[depth + 1 - length:depth + 1]:
                arr.pop()
                break
        else:
            dfs(depth + 1)
            arr.pop()
if n <= 6:
    print("".join(map(str, arr[:n])))
    exit()
dfs(6)