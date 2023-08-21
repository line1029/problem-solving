import io, os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
def main():
    n, k = map(int, input().split())
    arr = [0]*n
    for i in range(n):
        arr[i] = int(input())
    arr.sort()
    ans = arr[0]
    for i in range(1, n):
        if (arr[i] - arr[i - 1])*i <= k:
            ans = arr[i]
            k -= (arr[i] - arr[i - 1])*i
        else:
            ans += k//i
            break
    else:
        ans += k//n
    print(ans)
main()