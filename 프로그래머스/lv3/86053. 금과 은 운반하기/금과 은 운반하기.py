def solution(a, b, g, s, w, t):
    n = len(g)
    lo, hi = 1, (a + b)//min(w)*max(t)*3
    while lo < hi:
        mid = (lo + hi) >> 1
        weight_total = weight_gold = weight_silver = 0
        for i in range(n):
            weight = ((mid - t[i])//(t[i] << 1) + 1)*w[i]
            weight_total += weight if weight < g[i] + s[i] else g[i] + s[i]
            weight_gold += weight if weight < g[i] else g[i]
            weight_silver += weight if weight < s[i] else s[i]
        if weight_total >= a + b and weight_gold >= a and weight_silver >= b:
            hi = mid
        else:
            lo = mid + 1
    return lo
            