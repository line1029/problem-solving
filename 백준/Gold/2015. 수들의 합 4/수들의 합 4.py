from sys import stdin
def main():
    n, k = map(int, stdin.readline().split())
    ans = 0
    s = {0:1}
    psum = 0
    for i in map(int, stdin.readline().split()):
        psum += i
        target = psum - k
        if target in s:
            ans += s[target]
        if psum in s:
            s[psum] += 1
        else:
            s[psum] = 1
    print(ans)

main()