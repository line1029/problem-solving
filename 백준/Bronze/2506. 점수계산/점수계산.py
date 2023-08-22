from sys import stdin
def main():
    n = int(stdin.readline())
    score = 0
    cur = 0
    for i in map(int, stdin.readline().split()):
        cur *= i
        cur += i
        score += cur
    print(score)
main()