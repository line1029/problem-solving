from sys import stdin
def main():
    stdin.readline()
    x = 0
    more_than_1 = 0
    for i in map(int, stdin.readline().split()):
        if i > 1:
            more_than_1 += 1
        x ^= i
    if more_than_1:
        x = not x
    if x:
        print("cubelover")
    else:
        print("koosaga")

main()