import sys
n = int(sys.stdin.readline())
for i in range(n):
    res = sys.stdin.readline().rstrip()
    score = [0] * len(res)
    for idx, sym in enumerate(res):
        if sym == "O":
            score[idx] = score[idx - 1] + 1
    print(sum(score))
