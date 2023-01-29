from sys import stdin, stdout
n = int(stdin.readline())
adj_mat = list(map(lambda x: list(map(int, x.split())), stdin.readlines()))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_mat[i][k] and adj_mat[k][j]:
                adj_mat[i][j] = 1
stdout.write("\n".join(" ".join(map(str, row)) for row in adj_mat))