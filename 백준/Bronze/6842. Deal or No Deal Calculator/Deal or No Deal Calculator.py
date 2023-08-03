from sys import stdin
def main():
    cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
    n = 10 - int(stdin.readline())
    total = sum(cases)
    for _ in range(10 - n):
        total -= cases[int(stdin.readline()) - 1]
    total /= n

    if int(stdin.readline()) > total:
        print("deal")
    else:
        print("no deal")
main()
