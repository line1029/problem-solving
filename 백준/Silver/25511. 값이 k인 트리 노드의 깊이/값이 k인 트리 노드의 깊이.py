import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    n, k = input().split()
    n = int(n)
    parents = [0]*n
    for _ in range(n - 1):
        p, c = map(int, input().split())
        parents[c] = p
    k = input().split().index(k)
    depth = 0
    for _ in range(n):
        if not k:
            break
        k = parents[k]
        depth += 1
    print(depth)
main()