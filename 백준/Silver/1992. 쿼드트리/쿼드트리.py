from sys import stdin
n = int(stdin.readline())
data = list(map(lambda x: x.strip(), stdin.readlines()))

ans = []
def dfs(n, data):
    if n == 1:
        ans.append(data[0][0])
        return
    standard = data[0][0]
    for i in range(n):
        for j in range(n):
            if standard != data[i][j]:
                ans.append("(")
                for k in range(2):
                    for l in range(2):
                        dfs(n//2, [row[l*n//2:(l+1)*n//2] for row in data[k*n//2:(k+1)*n//2]])
                ans.append(")")
                return
    ans.append(standard)
dfs(n, data)
print("".join(ans))