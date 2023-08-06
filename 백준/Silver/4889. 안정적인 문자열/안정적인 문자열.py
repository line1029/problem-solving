from sys import stdin
def main():
    pars = stdin.read().splitlines()
    pars.pop()
    ans = []
    for par in pars:
        st = 0
        cnt = 0
        for char in par:
            if char == "{":
                st += 1
            else:
                st -= 1
                if st < 0:
                    st += 2
                    cnt += 1
        if st:
            cnt += (st >> 1)
        ans.append(cnt)
    print("\n".join(f"{idx}. {cnt}" for idx, cnt in enumerate(ans, 1)))
main()
