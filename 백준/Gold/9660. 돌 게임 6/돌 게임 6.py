def main():
    n = int(input())
    ans = [False, True, False, True, True, True, True]
    if ans[n%7]:
        print("SK")
    else:
        print("CY")
main()