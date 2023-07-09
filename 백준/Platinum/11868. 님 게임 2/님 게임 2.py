from sys import stdin
from functools import reduce
from operator import xor
def main():
    stdin.readline()
    if reduce(xor, map(int, stdin.readline().split())):
        print("koosaga")
    else:
        print("cubelover")

main()