from sys import stdin
import heapq
from collections import Counter
n = int(stdin.readline())
dasom = int(stdin.readline())
candidates = list(map(int, stdin.read().splitlines()))
c = Counter(candidates)
pq = [[-i, j] for i, j in c.items()]
heapq.heapify(pq)
ans = 0
if not pq or -pq[0][0] < dasom:
    print(ans)
    exit()

while True:
    num_votes, num_candidates = heapq.heappop(pq)
    num_votes = -num_votes
    if not pq:
        i = (num_votes - dasom) // (num_candidates + 1)
        j = min((num_votes - dasom) % (num_candidates + 1) + 1, num_candidates)
        ans += i*num_candidates + j
        print(ans)
        exit()
    nex_num_votes = -pq[0][0]
    if (num_votes - nex_num_votes) * num_candidates + dasom <= nex_num_votes:
        dasom += (num_votes - nex_num_votes) * num_candidates
        ans += (num_votes - nex_num_votes) * num_candidates
        pq[0][1] += num_candidates
        continue
    else:
        i = (num_votes - dasom) // (num_candidates + 1)
        j = min((num_votes - dasom) % (num_candidates + 1) + 1, num_candidates)
        ans += i*num_candidates + j
        print(ans)
        exit()
