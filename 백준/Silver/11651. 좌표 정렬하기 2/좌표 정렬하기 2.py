from sys import stdin, stdout

n = int(stdin.readline())
dots = sorted(map(lambda x: list(map(int, x.split())), stdin.readlines()), key=lambda x: (x[1], x[0]))

stdout.write("\n".join(" ".join(map(str, x)) for x in dots))
