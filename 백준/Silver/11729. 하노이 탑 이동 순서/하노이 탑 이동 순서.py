from sys import stdout, stdin
n = int(stdin.readline())
stdout.write(f"{2**n - 1}\n")
memo = dict()
def hanoi(start, end, spare, height):
    if (start, end, spare, height) in memo:
        return memo[(start, end, spare, height)]
    if height == 1:
        ans = f"{start} {end}\n"
        memo[(start, end, spare, height)] = ans
        return ans
    ans = hanoi(start, spare, end, height - 1) + f"{start} {end}\n" + hanoi(spare, end, start, height - 1)
    memo[(start, end, spare, height)] = ans
    return ans
stdout.write(hanoi(1, 3, 2, n))