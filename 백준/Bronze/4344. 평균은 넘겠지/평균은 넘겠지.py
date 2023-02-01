for i in range(int(input())):
    n, *scores = map(int, input().split())
    avg = sum(scores)/n
    over_avg = 0
    for score in scores:
        if score > avg:
            over_avg += 1
    ans = str(round(over_avg / n * 100, 3))
    if len(ans) == 3:
        ans += "0"
    while ans[-4] != ".":
        ans += "0"
    print(f"{ans}%")