from sys import stdin
def main():
    n = int(stdin.readline())
    st = m = cnt = 0
    for i in map(int, stdin.readline().split()):
        if i > st:
            cnt = 0
            st = i
        else:
            cnt += 1
            m = max(m, cnt)
    print(m)
main()