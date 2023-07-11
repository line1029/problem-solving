from sys import stdin
def main():
    bulbs = [0]*10
    for i, s in enumerate(stdin.read().splitlines()):
        for j, c in enumerate(s):
            if c == "O":
                bulbs[i] += (1 << (9 - j))
    ans = 101
    for i in range(1024):
        cnt = int.bit_count(i)
        cur_bulbs = bulbs[:]
        cur_bulbs[0] ^= (i^(i << 1)^(i >> 1))&1023
        cur_bulbs[1] ^= i
        for j in range(1, 10):
            cnt += int.bit_count(cur_bulbs[j - 1])
            cur_bulbs[j] ^= (cur_bulbs[j - 1]^(cur_bulbs[j - 1] << 1)^(cur_bulbs[j - 1] >> 1))&1023
            if j != 9:
                cur_bulbs[j + 1] ^= cur_bulbs[j - 1]
            cur_bulbs[j - 1] = 0
        if cnt < ans and not cur_bulbs[9]:
            ans = cnt
    if ans != 101:
        print(ans)
    else:
        print(-1)

main()