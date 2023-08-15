from sys import stdin
def main():
    j, y = -1, 0
    for i, x in enumerate(map(lambda x: sum(map(int, x.split())), stdin.read().splitlines())):
        if x > y:
            y = x
            j = i
    print(j + 1, y)
main()
