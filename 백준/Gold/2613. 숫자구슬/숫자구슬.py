from sys import stdin
from bisect import bisect_left
def main():
    n, m = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    def can_split(maxsum):
        cnt = 0
        num_groups = 1
        for num in arr:
            if cnt + num <= maxsum:
                cnt += num
            else:
                cnt = num
                num_groups += 1
            if num_groups > m:
                return False
        return True
    maxsum = bisect_left(list(range(sum(arr) + 1)), 1, lo=max(arr), key=can_split)
    print(maxsum)
    ans = []
    cur = 0
    cnt = 0
    for num in arr:
        if cur + num <= maxsum:
            cur += num
            cnt += 1
        else:
            ans.append(cnt)
            cur = num
            cnt = 1
    ans.append(cnt)
    if len(ans) < m:
        tmp = []
        need = m - len(ans)
        for idx, cnt in enumerate(ans):
            if cnt > 1:
                if cnt > need:
                    tmp += [1]*need
                    tmp.append(cnt - need)
                    break
                else:
                    tmp += [1]*cnt
                    need -= cnt - 1
            else:
                tmp.append(cnt)
        tmp += ans[idx + 1:]
        ans = tmp
    print(*ans)
main()