from sys import stdin, stdout
from collections import Counter
trees = stdin.read().splitlines()
n = len(trees)
trees = Counter(trees)
trees = (f"{i} {j/n * 100:.4f}" for i, j in sorted(trees.items()))
stdout.write("\n".join(trees))