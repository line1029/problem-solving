from sys import stdin
def main():
    n, m, r = map(int, stdin.readline().split())
    arr = list(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    for s in range(min(n, m) >> 1):
        tmp = []
        for i in range(s, n - s):
            tmp.append([i, s, arr[i][s]])
        for j in range(s + 1, m - s):
            tmp.append([n - s - 1, j, arr[n - s - 1][j]])
        for i in range(n - s - 2, s - 1, -1):
            tmp.append([i, m - s - 1, arr[i][m - s - 1]])
        for j in range(m - s - 2, s, -1):
            tmp.append([s, j, arr[s][j]])
        for i in range(len(tmp)):
            j = (i + r)%len(tmp)
            arr[tmp[j][0]][tmp[j][1]] = tmp[i][2]
    print("\n".join(" ".join(map(str, row)) for row in arr))
main()