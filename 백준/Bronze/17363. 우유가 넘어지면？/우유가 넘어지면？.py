from sys import stdin
import string
n, m = map(int, stdin.readline().split())
s = str.maketrans(r"-|/\^<v>", r"|-\/<v>^")
print('\n'.join(["".join(i) for i in zip(*stdin.read().translate(s).splitlines())][::-1]))