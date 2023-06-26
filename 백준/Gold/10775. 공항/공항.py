from sys import stdin, setrecursionlimit
setrecursionlimit(100001)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x):
    x = find(parent, x)
    if x:
        parent[x] = x - 1
        return True

def main():
    g = int(stdin.readline())
    p = int(stdin.readline())
    planes = list(map(int, stdin.read().splitlines()))
    parent = list(range(g + 1))
    ans = 0
    for i in range(min(g, p)):
        if union(parent, planes[i]):
            ans += 1
        else:
            break
    print(ans)

main()