from sys import stdin
def main():
    a, b, c = map(int, stdin.readline().split())
    x, y, z = map(int, stdin.readline().split())
    print(x - c, y//b, z - a)
main()