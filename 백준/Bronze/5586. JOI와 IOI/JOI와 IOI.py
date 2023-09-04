from sys import stdin
def main():
    s = input()
    arr = [s[i:i + 3] for i in range(len(s))]
    print(arr.count("JOI"))
    print(arr.count("IOI"))
main()