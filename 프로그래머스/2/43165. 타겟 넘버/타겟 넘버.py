from math import comb
from collections import Counter, defaultdict
from itertools import product
from functools import reduce
def solution(numbers, target):
    ans = 0
    num_cnts = Counter(numbers)
    partial_sums = defaultdict(list)
    for num, cnt in num_cnts.items():
        for i in range(cnt + 1):
            partial_sums[num].append((num*(2 * i - cnt), comb(cnt, i)))
    for pd in product(*partial_sums.values()):
        s, c = list(zip(*pd))
        if target != sum(s): continue
        ans += reduce(lambda x, y: x*y, c)
    return ans
    