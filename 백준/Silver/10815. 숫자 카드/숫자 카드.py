from sys import stdin, stdout
n = int(stdin.readline())
got = set(stdin.readline().split())
m = int(stdin.readline())
check = stdin.readline().split()
print(" ".join((str(int(i in got)) for i in check)))