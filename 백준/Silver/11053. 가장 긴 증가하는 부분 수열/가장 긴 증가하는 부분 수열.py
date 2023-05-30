from sys import stdin
from math import ceil, log2
def update(tree, tree_idx, start, end, seq_idx, max_val):
    if seq_idx < start or seq_idx > end:
        return
    if start == end == seq_idx:
        tree[tree_idx] = max_val
        return
    update(tree, tree_idx*2, start, (start+end)//2, seq_idx, max_val)
    update(tree, tree_idx*2+1, (start+end)//2+1, end, seq_idx, max_val)
    tree[tree_idx] = max(tree[tree_idx*2], tree[tree_idx*2+1])

def query(tree, tree_idx, start, end, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return tree[tree_idx]
    lmax = query(tree, tree_idx*2, start, (start+end)//2, left, right)
    rmax = query(tree, tree_idx*2+1, (start+end)//2+1, end, left, right)
    return max(lmax, rmax)
n = int(stdin.readline())
seq = map(int, stdin.readline().split())
h = ceil(log2(n)) + 1
tree_size = 1 << h
segment_tree = [0] * tree_size
for seq_idx, seq_val in sorted(enumerate(seq), key=lambda x: (x[1], -x[0])):
    max_lis = query(segment_tree, 1, 0, n-1, 0, seq_idx) + 1
    update(segment_tree, 1, 0, n-1, seq_idx, max_lis)
print(segment_tree[1])