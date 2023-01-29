from sys import stdout, stdin
n = int(stdin.readline())
# f(n) = f(n-1)*2 + 1
# f(1) = 1
# -> f(n) = 2**n - 1
stdout.write(f"{2**n - 1}\n")
if n > 20:
    exit()
memo = dict()
def hanoi(start, end, spare, height):
    if (start, end, spare, height) in memo:
        return memo[(start, end, spare, height)]
    if height == 1:
        ans = [f"{start} {end}"]
        memo[(start, end, spare, height)] = ans
        return ans
    ans = hanoi(start, spare, end, height - 1) + [f"{start} {end}"] + hanoi(spare, end, start, height - 1)
    memo[(start, end, spare, height)] = ans
    return ans
stdout.write("\n".join(hanoi(1, 3, 2, n)))