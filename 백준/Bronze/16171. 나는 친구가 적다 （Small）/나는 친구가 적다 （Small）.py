def main():
    import re
    s = re.sub("[\d]", "", input())
    ss = input()
    print(int(ss in s))
main()