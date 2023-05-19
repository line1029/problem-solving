# improved prim
from sys import stdin
import heapq
n = int(stdin.readline())
m = int(stdin.readline())
graph = [list() for _ in range(n + 1)]
for a, b, c in map(lambda x: map(int, x.split()), stdin.read().splitlines()):
    if a == b:
        continue
    graph[a].append((c, b))
    graph[b].append((c, a))


# implement binary heap with decrease key logic
def decrease_key(heap, node_idx):
    while node_idx:
        parent_idx = (node_idx - 1) >> 1
        if heap[parent_idx] < heap[node_idx]:
            break
        swap(heap, node_idx, parent_idx)
        node_idx = parent_idx


def swap(heap, i, j):
    heap[i], heap[j] = heap[j], heap[i]
    heap[i][2] = i
    heap[j][2] = j


def sift_down(heap, i):
    n = len(heap)
    while True:
        lo = i
        l = (i << 1) + 1
        r = (i + 1) << 1
        if l < n and heap[l][0] < heap[i][0]:
            lo = l
        if r < n and heap[r][0] < heap[lo][0]:
            lo = r
        
        if lo == i:
            break

        swap(heap, lo, i)
        i = lo


def extract_min(heap):
    last_elt = heap.pop()
    if heap:
        res = heap[0]
        heap[0] = last_elt
        last_elt[2] = 0
        sift_down(heap, 0)
        return res
    return last_elt


pq = [[10001, i + 1, i] for i in range(n)]
v_dict = {i+1:pq[i] for i in range(n)}
pq[0][0] = 0
ans = 0
while pq:
    weight, node, _ = extract_min(pq)
    ans += weight
    v_dict.pop(node)
    for edge in graph[node]:
        if edge[1] in v_dict:
            if v_dict[edge[1]][0] > edge[0]:
                v_dict[edge[1]][0] = edge[0]
                decrease_key(pq, v_dict[edge[1]][2])

print(ans)
