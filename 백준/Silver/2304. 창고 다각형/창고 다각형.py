from sys import stdin
input = stdin.readline
def main():
    n = int(input())
    arr = sorted(map(lambda x: list(map(int, x.split())), stdin.read().splitlines()))
    m = arr.index(max(arr, key=lambda x: x[1]))
    stack = []
    for i in range(m, n):
        while stack and stack[-1][1] < arr[i][1]:
            stack.pop()
        stack.append(arr[i])
    ans = sum((stack[i + 1][0] - stack[i][0])*stack[i + 1][1] for i in range(len(stack) - 1))
    stack = []
    for i in range(m, -1, -1):
        while stack and stack[-1][1] < arr[i][1]:
            stack.pop()
        stack.append(arr[i])
    ans += sum((stack[i][0] - stack[i + 1][0])*stack[i + 1][1] for i in range(len(stack) - 1))
    ans += arr[m][1]
    print(ans)
main()