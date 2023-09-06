from sys import stdin
input = stdin.readline
def main():
    n, k = map(int, input().split())
    students = [0]*5
    for s, y in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
        if y <= 2:
            students[0] += 1
        elif y <= 4:
            if s == 0:
                students[1] += 1
            else:
                students[2] += 1
        else:
            if s == 0:
                students[3] += 1
            else:
                students[4] += 1
    print(sum(i//k + (i%k != 0) for i in students))
main()