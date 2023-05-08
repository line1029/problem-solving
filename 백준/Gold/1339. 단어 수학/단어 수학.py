from sys import stdin
from collections import defaultdict, Counter
input = stdin.readline
n = int(input())
words = [[""]*8 for _ in range(n)]
word_to_num = defaultdict(int)
for i in range(n):
    word = input().strip()
    words[i][-len(word):] = list(word)
for i in range(8):
    candidates = Counter(words[j][i] for j in range(n))
    del candidates[""]
    for k, v in candidates.items():
        word_to_num[k] += v * 10**(7 - i)
ans = 0
for idx, (k, v) in enumerate(sorted(word_to_num.items(), key=lambda x: -x[1])):
    ans += v * (9 - idx)
print(ans)
