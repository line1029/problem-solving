from sys import stdin
def main():
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    if len(arr) == 2 and arr[0] == arr[1]:
        print(arr[0])
        exit()
    if len(arr) <= 2:
        print("A")
        exit()
    r1, r2 = arr[1] - arr[0], arr[2] - arr[1]
    if not r1:
        if len(set(arr)) != 1:
            print("B")
            exit()
        else:
            print(arr[0])
            exit()
    if r2%r1:
        print("B")
        exit()
    a = r2//r1
    b = arr[1] - arr[0]*a
    for i in range(3, n):
        if arr[i] != arr[i - 1]*a + b:
            print("B")
            exit()
    print(arr[-1]*a + b)
main()