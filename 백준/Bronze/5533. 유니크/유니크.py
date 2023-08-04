from sys import stdin
from collections import Counter
def main():
    n = int(stdin.readline())
    scores = [0]*n
    submits = map(lambda x: map(int, x.split()), stdin.read().splitlines())
    for submit in zip(*submits):
        c = Counter(submit)
        for idx, score in enumerate(submit):
            if c[score] == 1:
                scores[idx] += score
    print("\n".join(map(str, scores)))
main()
