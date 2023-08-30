def solution(a):
    n = len(a)
    lefta, righta = [0]*n, [0]*n
    lefta[0] = a[0]
    righta[-1] = a[-1]
    for i in range(1, n):
        lefta[i] = min(a[i], lefta[i - 1])
        righta[n - i - 1] = min(a[n - i - 1], righta[n - i])
    ans = 2
    for i in range(1, n - 1):
        if righta[i + 1] < a[i] > lefta[i - 1]: continue
        ans += 1
    return ans
    