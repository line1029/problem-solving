import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    n, q = map(int, input().split())
    tree = [0]*(n + 1)
    ans = [0]*q
    for idx in range(q):
        i = wanted = int(input())
        x = 0
        while i:
            if tree[i]:
                x = i
            i >>= 1
        ans[idx] = x
        if not x:
            tree[wanted] = 1
    print("\n".join(map(str, ans)))
main()