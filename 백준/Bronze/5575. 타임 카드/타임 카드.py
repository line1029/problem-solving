for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    h = eh - sh
    m = em - sm
    s = es - ss
    if s < 0:
        m -= 1
        s %= 60
    if m < 0:
        h -= 1
        m %= 60
    print(h, m, s)