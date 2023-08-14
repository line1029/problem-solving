from sys import stdin, stdout
def main():
    origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        t = str.maketrans(
            origin,
            "".join(origin[(a*i + b)%26] for i in range(26))
        )
        stdout.write(stdin.readline().translate(t))
main()