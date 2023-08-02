from sys import stdin
def main():
    n = int(stdin.readline())
    k = int(stdin.readline())
    if stdin.readline().count("R") == k:
        print("W")
    else:
        print("R")
main()