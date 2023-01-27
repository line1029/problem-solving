memo = dict()
def hanoi(start, end, spare, k):
    if (start, end, spare, k) in memo:
        return memo[(start, end, spare, k)]
    if k == 1:
        memo[(start, end, spare, k)] = [f"{start} {end}"]
        return memo[(start, end, spare, k)]
    if (start, spare, end, k-1) in memo:
        first = memo[(start, spare, end, k-1)]
    else:
        memo[(start, spare, end, k-1)] = hanoi(start, spare, end, k-1)
    ans = []
    ans += memo[(start, spare, end, k-1)]
    ans.append(f"{start} {end}")
    if (spare, end, start, k-1) in memo:
        first = memo[(spare, end, start, k-1)]
    else:
        memo[(spare, end, start, k-1)] = hanoi(spare, end, start, k-1)
    ans += memo[(spare, end, start, k-1)]
    memo[(start, end, spare, k)] = ans
    return ans

k = int(input())
print(2**k - 1)
print("\n".join(hanoi(1, 3, 2, k)))