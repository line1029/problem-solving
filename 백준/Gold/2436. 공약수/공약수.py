def main():
    from math import sqrt
    from itertools import product
    g, l = map(int, input().split())
    l //= g
    _min = l + 1
    ans = [1, l]
    candidate = []
    if not l & 1:
        tmp = 1
        while not l & 1:
            tmp <<= 1
            l >>= 1
        candidate.append(tmp)
    for i in range(3, int(l**.5) + 2, 2):
        if l % i == 0:
            tmp = 1
            while l % i == 0:
                l //= i
                tmp *= i
            candidate.append(tmp)
    candidate.append(l)
    k = len(candidate)
    for pat in product(range(2), repeat=k):
        a = b = 1
        for i in range(k):
            if pat[i]:
                a *= candidate[i]
            else:
                b *= candidate[i]
        if a + b < _min:
            _min = a + b
            ans = [min(a, b), max(a, b)]
    print(g*ans[0], g*ans[1])


main()