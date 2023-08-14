from sys import stdin, stdout
def main():
    ans = []
    origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for _ in range(int(stdin.readline())):
        a, b = map(int, stdin.readline().split())
        a %= 26
        b %= 26
        t = str.maketrans(
            origin,
            "".join(origin[(a*i + b)%26] for i in range(26))
        )
        ans.append(stdin.readline().translate(t))
    stdout.write("".join(ans))
main()