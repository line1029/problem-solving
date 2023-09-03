from sys import stdin
def main():
    n, m = map(int, stdin.readline().split())
    arr = list(range(n + 1))
    for i, j, k in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        arr[i:j + 1] = arr[k:j + 1] + arr[i:k]
    print(" ".join(map(str, arr[1:])))
main()