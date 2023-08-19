from sys import stdin
def main():
    arr = list(map(int, stdin.read().splitlines()))
    print(arr[0]*2 - sum(arr))
main()